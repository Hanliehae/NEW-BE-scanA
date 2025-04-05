from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Mahasiswa
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash
import os

admin_bp = Blueprint("admin", __name__)

@admin_bp.route('/mahasiswa', methods=['POST'])
def add_mahasiswa():
    # Ambil data dari form-data (karena ada file upload)
    nama_lengkap = request.form.get("nama_lengkap")
    nim = request.form.get("nim")
    email = request.form.get("email")
    password = generate_password_hash(request.form.get("password"))
    no_telepon = request.form.get("no_telepon")
    mata_kuliah = request.form.get("mata_kuliah")

    # Ambil file upload
    foto_kiri = request.files.get("foto_tangan_kiri")
    foto_kanan = request.files.get("foto_tangan_kanan")
    foto_wajah = request.files.get("foto_wajah")

    # Fungsi simpan file
    def simpan_file(file, folder):
        if file:
            filename = secure_filename(file.filename)
            path = os.path.join("uploads", folder, filename)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            file.save(path)
            return path
        return None

    path_kiri = simpan_file(foto_kiri, "tangan_kiri")
    path_kanan = simpan_file(foto_kanan, "tangan_kanan")
    path_wajah = simpan_file(foto_wajah, "wajah")

    # Simpan ke DB
    mahasiswa = Mahasiswa(
        nama_lengkap=nama_lengkap,
        nim=nim,
        email=email,
        password=password,
        no_telepon=no_telepon,
        mata_kuliah=mata_kuliah,
        foto_tangan_kiri=path_kiri,
        foto_tangan_kanan=path_kanan,
        foto_wajah=path_wajah
    )
    db.session.add(mahasiswa)
    db.session.commit()

    return jsonify({"message": "Mahasiswa berhasil ditambahkan"}), 201
