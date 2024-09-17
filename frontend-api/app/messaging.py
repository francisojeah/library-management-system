import pika
import os
import json
from .database import SessionLocal
from .models import Book

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", 5672))

def add_book_to_catalog(book_data):
    try:
        book = json.loads(book_data)
        with SessionLocal() as db:
            db_book = Book(
                id=book['id'],
                title=book['title'],
                category=book['category'],
                publisher=book['publisher'],
                available=book['available']
            )
            db.add(db_book)
            db.commit()
    except Exception as e:
        print(f"Error adding book to catalog: {e}")

def on_message(ch, method, properties, body):
    # Process the book update
    book_data = body.decode("utf-8")
    add_book_to_catalog(book_data)

def start_consuming():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT))
        channel = connection.channel()
        channel.queue_declare(queue='book_updates')

        print('Waiting for messages. To exit press CTRL+C')
        channel.basic_consume(queue='book_updates', on_message_callback=on_message, auto_ack=True)
        channel.start_consuming()
    except Exception as e:
        print(f"Error in RabbitMQ connection or consumption: {e}")
