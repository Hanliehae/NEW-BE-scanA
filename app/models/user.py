from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nama_lengkap = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # "admin" atau "mahasiswa"
        
    # Relasi ke Mahasiswa (jika role = mahasiswa)
    mahasiswa = relationship("Mahasiswa", back_populates="user", uselist=False)

    # Properti password dan verifikasi hash
    @property
    def password(self):
        raise AttributeError("Password is not readable!")

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.email} ({self.role})>"