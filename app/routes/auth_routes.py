from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import User
from werkzeug.security import generate_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
import re

auth_bp = Blueprint("auth", __name__)

# CEK PASSWORD KUAT
def is_password_strong(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):  # huruf besar
        return False
    if not re.search(r"[a-z]", password):  # huruf kecil
        return False
    if not re.search(r"[0-9]", password):  # angka
        return False
    return True

#  REGISTER MAHASISWA
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Email dan password wajib diisi"}), 400

    if not is_password_strong(data["password"]):
        return jsonify({
            "error": "Password harus minimal 8 karakter, mengandung huruf besar, huruf kecil, dan angka."
        }), 400

    # Cek apakah email sudah ada
    existing_user = User.query.filter_by(email=data["email"]).first()
    if existing_user:
        return jsonify({"error": "Email sudah terdaftar"}), 409
    
    hashed_password = generate_password_hash(data["password"])
    new_user = User(
        nama_lengkap=data.get("nama_lengkap"),
        email=data["email"],
        nim=data.get("nim"),
        password_hash=hashed_password,
        role="mahasiswa"
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User berhasil terdaftar"}), 201

# LOGIN UNTUK ADMIN & MAHASISWA
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Email dan password wajib diisi"}), 400

    user = User.query.filter_by(email=data["email"]).first()

    if not user or not check_password_hash(user.password_hash, data["password"]):
        return jsonify({"error": "Email atau password salah"}), 401

    return jsonify({
        "message": "Login berhasil",
        "user_id": user.id,
        "nama": user.nama_lengkap,
        "email": user.email,
        "role": user.role
    }), 200
