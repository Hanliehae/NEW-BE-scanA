def authenticate_user(nim, password):
    if nim == "12345" and password == "password":
        return {"nim": nim, "token": "mock_token"}
    return None
