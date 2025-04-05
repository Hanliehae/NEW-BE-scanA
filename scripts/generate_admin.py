import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app
from app.extensions import db
from app.models.user import User
app = create_app()

with app.app_context():
    existing = User.query.filter_by(email="dosen@example.com").first()
    if not existing:
        user = User(
            nama_lengkap="Dosen A",
            email="dosen@example.com",
            role="admin"
        )
        user.password = "admin123"  # setter ini akan langsung hash password-nya
        db.session.add(user)
        db.session.commit()
        print("✅ Admin berhasil dibuat!")
    else:
        print("⚠️ Admin dengan email ini sudah ada.")
