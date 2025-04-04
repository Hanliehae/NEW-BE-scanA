from app.extensions import db
from datetime import datetime

class Kehadiran(db.Model):
    __tablename__ = 'kehadiran'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    jadwal_id = db.Column(db.Integer, db.ForeignKey('jadwal.id'), nullable=False)
    waktu_scan = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status = db.Column(db.String(10), nullable=False)  # "Hadir" atau "Absen"
