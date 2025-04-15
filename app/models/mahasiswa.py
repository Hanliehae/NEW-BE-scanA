
from app.extensions import db
from sqlalchemy.orm import relationship

class Mahasiswa(db.Model):
    __tablename__ = 'mahasiswa'

    nim = db.Column(db.String(20), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    no_telepon = db.Column(db.String(20))
    mata_kuliah = db.Column(db.String(100))

    foto_tangan_kiri = db.Column(db.String(200))
    foto_tangan_kanan = db.Column(db.String(200))
    foto_wajah = db.Column(db.String(200))

     # Relasi ke User
    user = relationship("User", back_populates="mahasiswa")

    # Relasi ke Kehadiran
    riwayat_kehadiran = relationship("Kehadiran", backref='mahasiswa', lazy=True)

    def __repr__(self):
        return f"<Mahasiswa {self.nim}>"
