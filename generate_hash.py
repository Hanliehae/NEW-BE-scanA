from werkzeug.security import generate_password_hash

# Ganti password ini sesuai kebutuhan
plain_password = "admin123"

# Generate hash-nya
hashed_password = generate_password_hash(plain_password)

# Tampilkan hasilnya
print("Password asli:", plain_password)
print("Password hash:", hashed_password)
