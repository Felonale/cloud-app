from app import app

def test_addition():
    assert 2 + 2 == 4

def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Cloud Technologies" in response.data
