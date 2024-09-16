# Library Management System

This project is a library management system that consists of two independent API services:
1. **Frontend API** - For user interactions such as browsing books, borrowing books, and user enrollment.
2. **Admin API** - For administrative tasks such as adding/removing books, listing users, and managing borrowed books.

The APIs communicate using a message broker (RabbitMQ) to synchronize data between the services.

## Features

### Frontend API:
- User enrollment (email, first name, last name).
- Browse the library's book catalog.
- Get details of a single book by its ID.
- Filter books by publisher or category.
- Borrow books by specifying the borrowing period.

### Backend/Admin API:
- Add new books to the library.
- Remove books from the catalog.
- Fetch users enrolled in the library.
- List borrowed books and their return dates.
- Sync book availability between services using RabbitMQ.

## Tech Stack
- **FastAPI**: Python framework for building APIs.
- **PostgreSQL**: Database for the Frontend API.
- **MongoDB**: Database for the Admin API.
- **RabbitMQ**: Message broker for syncing changes between services.
- **Docker**: Containerization for easy deployment.
- **Pytest**: Unit and integration testing.

## Setup and Deployment

### Prerequisites
- Docker and Docker Compose
- Python 3.x
- PostgreSQL and MongoDB installed (optional if not using Docker)

### Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/francisojeah/library-management-system.git
   cd library-management-system
   ```

2. Install dependencies for both services:
   ```bash
   cd frontend-api
   pip install -r requirements.txt
   cd ../admin-api
   pip install -r requirements.txt
   ```

3. Start the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```

4. The APIs will be available at:
   - Frontend API: `http://localhost:8000`
   - Admin API: `http://localhost:8001`

### Running Tests
To run unit and integration tests:
```bash
docker-compose run frontend-api pytest
docker-compose run admin-api pytest
```

### API Documentation
- FastAPI provides automatic API documentation:
  - Frontend API docs: `http://localhost:8000/docs`
  - Admin API docs: `http://localhost:8001/docs`
