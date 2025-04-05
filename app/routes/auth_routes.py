from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import User
from werkzeug.security import generate_password_hash

auth_bp = Blueprint("auth", __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Email dan password wajib diisi"}), 400

    hashed_password = generate_password_hash(data["password"])
    new_user = User(email=data["email"], password_hash=hashed_password, role="mahasiswa")

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User berhasil terdaftar"}), 201
