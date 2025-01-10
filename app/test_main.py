from fastapi.testclient import TestClient
from httpx import WSGITransport
from main import app

transport = WSGITransport(app=app)
client = TestClient(transport=transport)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Masterclass Overview MLOPS"}
