from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_book():
    response = client.post("/books/", json={"title": "Test Book", "category": "Fiction", "publisher": "Test Publisher"})
    assert response.status_code == 200
    assert response.json()["message"] == "Book added successfully"
