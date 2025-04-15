from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
from app.models import Jadwal, Kehadiran, User
from app.extensions import db
from datetime import datetime
from zoneinfo import ZoneInfo
from app.services.inference import predict_identity

scan_bp = Blueprint('scan_bp', __name__)
UPLOAD_FOLDER = "app/static/uploads"

@scan_bp.route('/scan', methods=['POST'])
def scan_tangan():
    if 'image' not in request.files:
        return jsonify({"error": "Gambar tidak ditemukan"}), 400

    file = request.files['image']
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Prediksi identitas mahasiswa berdasarkan gambar tangan
    predicted_nim = predict_identity(filepath)
    if not predicted_nim:
        return jsonify({"error": "Mahasiswa tidak dikenali"}), 404

    # Ambil user berdasarkan NIM
    user = User.query.filter_by(nim=predicted_nim).first()
    if not user:
        return jsonify({"error": "User tidak ditemukan"}), 404


    # Ambil waktu Asia/Makassar (Manado)
    waktu_sekarang = datetime.now(ZoneInfo("Asia/Makassar"))
    waktu_scan = waktu_sekarang.time()
    today = waktu_sekarang.date()

     # Cari jadwal aktif saat ini
    jadwal = Jadwal.query.filter(
        Jadwal.tanggal == today,
        Jadwal.jam_mulai <= waktu_scan,
        Jadwal.jam_selesai >= waktu_scan
    ).first()

    if not jadwal:
        return jsonify({"message": "Tidak ada jadwal aktif saat ini"}), 404

    # Cek apakah user sudah absen
    sudah_absen = Kehadiran.query.filter_by(user_id=user.id, jadwal_id=jadwal.id).first()
    if sudah_absen:
        return jsonify({"message": "Sudah absen sebelumnya"}), 400

    # Simpan kehadiran dengan waktu scan lokal
    kehadiran = Kehadiran(
        user_id=user.id,
        jadwal_id=jadwal.id,
        waktu_scan=waktu_sekarang,
        status='hadir'
    )
    db.session.add(kehadiran)
    db.session.commit()

    return jsonify({
        "message": "Presensi berhasil dicatat",
        "nim": predicted_nim,
        "nama": user.nama_lengkap,
        "jadwal_id": jadwal.id,
        "waktu_scan": waktu_sekarang.strftime('%Y-%m-%d %H:%M:%S')
    }), 201
