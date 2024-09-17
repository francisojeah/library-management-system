from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_enroll_user():
    response = client.post("/users/", json={"email": "test@example.com", "firstname": "Test", "lastname": "User"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_list_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
