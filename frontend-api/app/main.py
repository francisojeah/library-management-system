from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import User, Book, Base
from .database import SessionLocal, engine, get_db
from .schemas import UserCreate 
from threading import Thread
from .messaging import start_consuming

app = FastAPI()

@app.on_event("startup")
def startup_event():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)

    # Start a separate thread to run the RabbitMQ consumer
    thread = Thread(target=start_consuming)
    thread.daemon = True
    thread.start()

@app.post("/users/")
def enroll_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(email=user.email, firstname=user.firstname, lastname=user.lastname)
    db.add(db_user)
    db.commit()
    return db_user

@app.get("/books/")
def list_books(db: Session = Depends(get_db)):
    books = db.query(Book).filter(Book.available == True).all()
    return books

@app.get("/books/{id}")
def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books/{id}/borrow")
def borrow_book(id: int, days: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if not book or not book.available:
        raise HTTPException(status_code=400, detail="Book is not available")
    book.available = False
    db.commit()
    return {"message": f"Book borrowed for {days} days"}

def add_book_to_catalog(book_data):
    # Implement the function to update the catalog with the new book
    pass
