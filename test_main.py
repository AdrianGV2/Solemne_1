from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_time():
    response = client.get("/time")
    assert response.status_code == 200
    assert "timezone_offset" in response.json()
