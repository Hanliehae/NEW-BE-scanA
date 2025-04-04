from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'  # Nama tabel yang lebih eksplisit

    id = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(100), nullable=False)
    nim = db.Column(db.String(20), unique=True, nullable=True)  # NIM hanya untuk mahasiswa
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # "admin" atau "mahasiswa"

    # Relasi ke Kehadiran
    kehadiran = db.relationship('Kehadiran', backref='user', lazy=True)


class MataKuliah(db.Model):
    __tablename__ = 'mata_kuliah'

    id = db.Column(db.Integer, primary_key=True)
    kode_mk = db.Column(db.String(20), unique=True, nullable=False)
    nama_mk = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.String(10), nullable=False)

    # Relasi ke Jadwal
    jadwal = db.relationship('Jadwal', backref='mata_kuliah', lazy=True)


class Jadwal(db.Model):
    __tablename__ = 'jadwal'

    id = db.Column(db.Integer, primary_key=True)
    mata_kuliah_id = db.Column(db.Integer, db.ForeignKey('mata_kuliah.id'), nullable=False)
    pertemuan_ke = db.Column(db.Integer, nullable=False)
    tanggal = db.Column(db.Date, nullable=False)
    jam_mulai = db.Column(db.Time, nullable=False)
    jam_selesai = db.Column(db.Time, nullable=False)

    # Relasi ke Kehadiran
    kehadiran = db.relationship('Kehadiran', backref='jadwal', lazy=True)


class Kehadiran(db.Model):
    __tablename__ = 'kehadiran'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    jadwal_id = db.Column(db.Integer, db.ForeignKey('jadwal.id'), nullable=False)
    waktu_scan = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status = db.Column(db.String(10), nullable=False)  # "Hadir" atau "Absen"
