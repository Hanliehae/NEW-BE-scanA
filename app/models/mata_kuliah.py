from app import db

class MataKuliah(db.Model):
    __tablename__ = 'mata_kuliah'

    id = db.Column(db.Integer, primary_key=True)
    kode_mk = db.Column(db.String(20), unique=True, nullable=False)
    nama_mk = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.String(10), nullable=False)

    # Relasi ke Jadwal
    jadwal = db.relationship('Jadwal', backref='mata_kuliah', lazy=True)
