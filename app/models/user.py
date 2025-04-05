from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

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

    # 🔐 Properti password dan verifikasi hash
    @property
    def password(self):
        raise AttributeError("Password is not readable!")

    @password.setter
    def password(self, plain_text):
        self.password_hash = generate_password_hash(plain_text)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
