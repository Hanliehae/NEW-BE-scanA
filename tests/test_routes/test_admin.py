def test_get_mahasiswa(client):
    response = client.get('/admin/mahasiswa')
    assert response.status_code in [200, 404]  # 404 jika belum ada mahasiswa

def test_add_mahasiswa(client):
    response = client.post('/admin/mahasiswa', json={
        "nama_lengkap": "Mahasiswa Baru",
        "nim": "9876543210",
        "email": "mahasiswa@example.com",
        "password": "password123",
        "mata_kuliah": ["MK001"],
        "foto_tangan_kiri": "base64encodedstring",
        "foto_tangan_kanan": "base64encodedstring",
        "foto_wajah": "base64encodedstring"
        
    })
    assert response.status_code in [200, 201]
