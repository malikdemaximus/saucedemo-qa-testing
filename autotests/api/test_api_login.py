import requests

def test_api_login():
    url = "https://api.saucedemo.com/login"
    data = {"username": "standard_user", "password": "secret_sauce"}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert "access_token" in response.json()
