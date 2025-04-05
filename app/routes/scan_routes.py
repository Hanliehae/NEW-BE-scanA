from flask import Blueprint, request, jsonify
from app.models import Jadwal, Kehadiran, User
from app.extensions import db
from datetime import datetime
from pytz import timezone

scan_bp = Blueprint('scan_bp', __name__)

@scan_bp.route('/', methods=['POST'])
def scan_tangan():
    data = request.json
    user_id = data.get('user_id')

    # Ambil waktu Asia/Makassar (Manado)
    waktu_sekarang = datetime.now(timezone('Asia/Makassar'))
    waktu_scan = waktu_sekarang.time()
    today = waktu_sekarang.date()

    # Cari jadwal yang sesuai
    jadwal = Jadwal.query.filter(
        Jadwal.tanggal == today,
        Jadwal.jam_mulai <= waktu_scan,
        Jadwal.jam_selesai >= waktu_scan
    ).first()

    if not jadwal:
        return jsonify({"message": "Tidak ada jadwal aktif saat ini"}), 404

    # Cek apakah user sudah absen
    sudah_absen = Kehadiran.query.filter_by(user_id=user_id, jadwal_id=jadwal.id).first()
    if sudah_absen:
        return jsonify({"message": "Sudah absen sebelumnya"}), 400

    # Simpan kehadiran dengan waktu scan lokal
    kehadiran = Kehadiran(
        user_id=user_id,
        jadwal_id=jadwal.id,
        waktu_scan=waktu_sekarang,
        status='hadir'
    )
    db.session.add(kehadiran)
    db.session.commit()

    return jsonify({
        "message": "Presensi berhasil dicatat",
        "jadwal_id": jadwal.id,
        "waktu_scan": waktu_sekarang.strftime('%Y-%m-%d %H:%M:%S')
    }), 201
