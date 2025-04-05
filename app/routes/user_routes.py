# routes/user_routes.py
from flask import Blueprint, request, jsonify
from app.models import Kehadiran, Jadwal, MataKuliah
from app.extensions import db
from datetime import datetime

user_bp = Blueprint('user', __name__)

@user_bp.route('/riwayat', methods=['GET'])
def lihat_riwayat():
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({"error": "user_id diperlukan"}), 400

    kehadiran = Kehadiran.query.filter_by(user_id=user_id).join(Jadwal).all()

    hasil = []
    for k in kehadiran:
        hasil.append({
            "tanggal": k.jadwal.tanggal.strftime("%Y-%m-%d") if k.jadwal.tanggal else None,
            "jam_mulai": k.jadwal.jam_mulai.strftime("%H:%M") if k.jadwal.jam_mulai else None,
            "jam_selesai": k.jadwal.jam_selesai.strftime("%H:%M") if k.jadwal.jam_selesai else None,
            "status": k.status,
            "mata_kuliah": k.jadwal.mata_kuliah.nama if k.jadwal.mata_kuliah else None
        })

    return jsonify(hasil), 200
