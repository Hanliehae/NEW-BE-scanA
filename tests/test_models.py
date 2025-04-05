from app.models.mahasiswa import Mahasiswa
from app import db

def test_create_mahasiswa(app):
    with app.app_context():
        mhs = Mahasiswa(nama="Test", nim="9999", email="test@mail.com", password_hash="hashed")
        db.session.add(mhs)
        db.session.commit()

        assert mhs.id is not None
        assert Mahasiswa.query.count() == 1
