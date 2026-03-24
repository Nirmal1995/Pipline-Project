import app

def test_health():
    client = app.app.test_client()
    response = client.get("/health")
    assert response.status_code == 200