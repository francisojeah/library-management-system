from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from .models import Book
from bson import ObjectId
from .messaging import notify_book_added
from .database import db

app = FastAPI()

@app.post("/books/")
async def add_book(book: Book):
    # Logic to add book to MongoDB
    collection = db["books"]
    new_book = book.dict()
    await collection.insert_one(new_book)

    # Notify Frontend API about the new book
    notify_book_added(new_book)

    return {"message": "Book added successfully"}

@app.delete("/books/{id}")
async def remove_book(id: str):
    collection = db["books"]
    result = await collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book removed successfully"}

@app.get("/users/")
async def list_users():
    users_collection = db["users"]
    users = await users_collection.find().to_list(length=100)
    return users
