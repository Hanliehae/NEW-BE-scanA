from flask import Blueprint, jsonify

scan_bp = Blueprint('scan', __name__)

@scan_bp.route('/detect', methods=['POST'])
def detect():
    return jsonify({"message": "Deteksi Telapak Tangan Berhasil"})
