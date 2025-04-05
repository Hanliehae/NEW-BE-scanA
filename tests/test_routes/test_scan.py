def test_scan_tangan(client):
    response = client.post('/scan', json={
        "image_data": "fake_base64_image_data"
    })
    assert response.status_code in [200, 400]
