import pytest
from app.database import db
from app.models import Book

@pytest.mark.asyncio
async def test_add_book():
    collection = db["books"]
    new_book = Book(title="Test Book", category="Fiction", publisher="Test Publisher")
    await collection.insert_one(new_book.dict())

    book = await collection.find_one({"title": "Test Book"})
    assert book is not None
    assert book["title"] == "Test Book"
