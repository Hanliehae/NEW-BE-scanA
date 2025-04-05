from app import create_app
from app.extensions import db
from app.models.user import User

app = create_app()

with app.app_context():
    user = User(
        nama_lengkap="Dosen A",
        email="dosen@example.com",
        role="admin"
    )
    user.password = "admin123"  # 🔐 ini otomatis di-hash

    db.session.add(user)
    db.session.commit()
    print("✅ Admin berhasil ditambahkan.")
