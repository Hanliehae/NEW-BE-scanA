# app/models/mahasiswa.py
from app.extensions import db

class Mahasiswa(db.Model):
    __tablename__ = 'mahasiswa'

    id = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(100), nullable=False)
    nim = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # disimpan dalam bentuk hashed
    no_telepon = db.Column(db.String(20))
    mata_kuliah = db.Column(db.String(100))

    foto_tangan_kiri = db.Column(db.String(200))
    foto_tangan_kanan = db.Column(db.String(200))
    foto_wajah = db.Column(db.String(200))

    riwayat_kehadiran = db.relationship('Kehadiran', backref='mahasiswa', lazy=True)
