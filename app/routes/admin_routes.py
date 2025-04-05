from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Mahasiswa

admin_bp = Blueprint("admin", __name__)

@admin_bp.route('/mahasiswa', methods=['GET', 'POST'])
def add_mahasiswa():
    data = request.get_json()
    new_mahasiswa = Mahasiswa(
        nama_lengkap=data["nama_lengkap"],
        nim=data["nim"],
        email=data["email"],
        password=data["password"],  # Note: harus di-hash di model
    )
    db.session.add(new_mahasiswa)
    db.session.commit()
    return jsonify({"message": "Mahasiswa ditambahkan"}), 201
