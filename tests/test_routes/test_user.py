def test_get_riwayat(client):
    response = client.get('/user/riwayat/1')  # asumsi user_id = 1
    assert response.status_code in [200, 404]
