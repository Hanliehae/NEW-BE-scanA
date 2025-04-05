from flask import Blueprint, request, jsonify

scan_bp = Blueprint("scan", __name__)

@scan_bp.route('', methods=['POST'])
def scan_tangan():
    data = request.get_json()
    if "image_data" not in data:
        return jsonify({"error": "Gambar tidak ditemukan"}), 400
    
    return jsonify({"message": "Scan berhasil"}), 200
