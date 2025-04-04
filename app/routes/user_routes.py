from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])
def profile():
    return jsonify({"message": "Profile Mahasiswa"})
