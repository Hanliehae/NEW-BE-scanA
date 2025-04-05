from app.extensions import db

class MataKuliah(db.Model):
    __tablename__ = 'mata_kuliah'

    id = db.Column(db.Integer, primary_key=True)
    kode_mk = db.Column(db.String(10), nullable=False)
    nama_mk = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    tahun_akademik = db.Column(db.String(10), nullable=False)
