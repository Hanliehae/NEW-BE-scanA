def test_register(client):
    response = client.post('/auth/register', json={
        "nama_lengkap": "Test User",
        "nim": "1234567890",
        "email": "test@example.com",
        "password": "password123",
        "role": "mahasiswa"
    })
    assert response.status_code in [200, 201]

def test_login(client):
    client.post('/auth/register', json={
        "nama_lengkap": "Test User",
        "nim": "1234567890",
        "email": "test@example.com",
        "password": "password123",
        "role": "mahasiswa"
    })
    
    response = client.post('/auth/login', json={
        "email": "test@example.com",
        "password": "password123"
    })
    assert response.status_code == 200
    assert "token" in response.get_json()
