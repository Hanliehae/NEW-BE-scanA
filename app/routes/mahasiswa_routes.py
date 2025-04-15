import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app.extensions import db
from app.models.user import User
from app.models.mahasiswa import Mahasiswa

mahasiswa_bp = Blueprint('mahasiswa', __name__)

UPLOAD_FOLDER = 'uploads'

@mahasiswa_bp.route('/register', methods=['POST'])
def register_mahasiswa():
    try:
        data = request.form
        nim = data.get('nim')
        nama = data.get('nama_lengkap')
        email = data.get('email')
        password = data.get('password')
        no_telepon = data.get('no_telepon')
        mata_kuliah = data.get('mata_kuliah')

        # Cek jika email atau nim sudah terdaftar
        if User.query.filter_by(email=email).first():
            return jsonify({'message': 'Email sudah terdaftar'}), 400
        if Mahasiswa.query.filter_by(nim=nim).first():
            return jsonify({'message': 'NIM sudah terdaftar'}), 400

        # Simpan ke tabel users
        user = User(nama_lengkap=nama, email=email, role="mahasiswa")
        user.password = password
        db.session.add(user)
        db.session.commit()

        # Simpan file foto
        def simpan_file(field_name, subfolder):
            file = request.files.get(field_name)
            if file:
                filename = secure_filename(file.filename)
                path = os.path.join(UPLOAD_FOLDER, subfolder)
                os.makedirs(path, exist_ok=True)
                file_path = os.path.join(path, filename)
                file.save(file_path)
                return file_path
            return None

        foto_kiri = simpan_file('foto_tangan_kiri', 'tangan_kiri')
        foto_kanan = simpan_file('foto_tangan_kanan', 'tangan_kanan')
        foto_wajah = simpan_file('foto_wajah', 'wajah')

        # Simpan ke tabel mahasiswa
        mahasiswa = Mahasiswa(
            nim=nim,
            user_id=user.id,
            no_telepon=no_telepon,
            mata_kuliah=mata_kuliah,
            foto_tangan_kiri=foto_kiri,
            foto_tangan_kanan=foto_kanan,
            foto_wajah=foto_wajah
        )
        db.session.add(mahasiswa)
        db.session.commit()

        return jsonify({'message': 'Registrasi mahasiswa berhasil'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500