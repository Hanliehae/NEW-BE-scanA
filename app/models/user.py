from app.models import db
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(100), nullable=False)
    nim = db.Column(db.String(20), unique=True, nullable=True)  
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # "admin" atau "mahasiswa"

    # Relasi ke Kehadiran
    kehadiran = db.relationship('Kehadiran', backref='user', lazy=True)
