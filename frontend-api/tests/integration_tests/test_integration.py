from fastapi.testclient import TestClient
from admin_api.app.main import app as admin_app
from frontend_api.app.main import app as frontend_app

admin_client = TestClient(admin_app)
frontend_client = TestClient(frontend_app)

def test_add_book_sync():
    response = admin_client.post("/books/", json={"title": "Integration Test Book", "category": "Science", "publisher": "Integration Publisher"})
    assert response.status_code == 200

    response = frontend_client.get("/books/")
    books = response.json()
    assert any(book["title"] == "Integration Test Book" for book in books)
