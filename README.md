# Library Management System

This project is a library management system consisting of two independent API services:
1. **Frontend API**: Handles user interactions such as browsing and borrowing books, as well as user management.
2. **Admin API**: Manages administrative tasks such as adding/removing books, managing users, and handling borrowed books.

Both APIs communicate using **RabbitMQ** to synchronize data between the services, ensuring real-time updates for book availability and user actions.

## Features

### Frontend API
- **User Enrollment**: Register users with their email, first name, and last name.
- **Browse Books**: Retrieve a list of books from the library catalog.
- **Book Details**: Fetch details of a specific book by its ID.
- **Filter Books**: Search for books by category or publisher.
- **Borrow Books**: Allow users to borrow books for a specified period.

### Admin API
- **Add Books**: Add new books to the library's catalog.
- **Remove Books**: Delete books from the catalog.
- **List Users**: Retrieve a list of users registered in the library system.
- **Manage Borrowed Books**: View which books are borrowed and manage their return dates.
- **Data Sync via RabbitMQ**: Keep book availability synchronized between the services using RabbitMQ.

## Tech Stack
- **FastAPI**: Python framework for building APIs.
- **PostgreSQL**: Relational database used by the Frontend API.
- **MongoDB**: NoSQL database used by the Admin API.
- **RabbitMQ**: Message broker used to synchronize changes between the services.
- **Docker**: Containerization for both APIs, databases, and RabbitMQ.
- **Pytest**: For unit and integration testing.

## System Architecture
- **Frontend API**: Communicates with PostgreSQL and RabbitMQ.
- **Admin API**: Communicates with MongoDB and RabbitMQ.
- **RabbitMQ**: Ensures data consistency between the Frontend and Admin APIs.

## Setup and Deployment

### Prerequisites
- **Docker** and **Docker Compose** installed.
- Optionally, **Python 3.x**, **PostgreSQL**, and **MongoDB** installed for local development without Docker.

### Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/francisojeah/library-management-system.git
   cd library-management-system
   ```

2. **Create environment variables**:
   Add `.env` files for both services as described below:

   **frontend-api/.env**
   ```bash
   DATABASE_URL=postgresql://postgres:password@postgres:5432/library_frontend
   RABBITMQ_HOST=rabbitmq
   ```

   **admin-api/.env**
   ```bash
   MONGODB_URL=mongodb://mongo:27017/library_admin
   RABBITMQ_HOST=rabbitmq
   ```

3. **Start the services** using Docker Compose:
   ```bash
   docker-compose up --build
   ```

   This will launch the following containers:
   - **frontend-api**: Available at `http://localhost:8000`
   - **admin-api**: Available at `http://localhost:8001`
   - **PostgreSQL**: Database for the Frontend API.
   - **MongoDB**: Database for the Admin API.
   - **RabbitMQ**: Available at `http://localhost:15672` (guest/guest login).

### Accessing the APIs
- **Frontend API Documentation**: `http://localhost:8000/docs`
- **Admin API Documentation**: `http://localhost:8001/docs`
- **RabbitMQ Management**: `http://localhost:15672`

### Running Tests
To run tests for both services, use the following commands:

1. **Frontend API Tests**:
   ```bash
   docker-compose exec frontend-api pytest
   ```

2. **Admin API Tests**:
   ```bash
   docker-compose exec admin-api pytest
   ```

Ensure that your test cases are placed in `tests/` directories inside both `frontend-api/` and `admin-api/` folders, and that you have added tests for both unit and integration tests.

## Project Structure

```bash
.
├── admin-api
│   ├── app/                   # Admin API application code
│   ├── Dockerfile              # Docker configuration for admin API
│   ├── requirements.txt        # Dependencies for admin API
│   ├── tests/                  # Tests for admin API
│   └── .env                    # Environment variables for admin API (not included in repo)
├── frontend-api
│   ├── app/                    # Frontend API application code
│   ├── Dockerfile              # Docker configuration for frontend API
│   ├── requirements.txt        # Dependencies for frontend API
│   ├── tests/                  # Tests for frontend API
│   └── .env                    # Environment variables for frontend API (not included in repo)
├── docker-compose.yml           # Docker Compose file for orchestrating services
├── README.md                    # Project documentation
└── .gitignore                   # Ignored files (including .env)
```

## Contribution Guide
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a clear description of the changes.

## Continuous Integration

This project uses **GitHub Actions** for continuous integration. The tests for both the Frontend and Admin APIs are automatically executed on every push or pull request to the `main` branch. The CI pipeline builds the Docker containers and runs the tests to ensure the code is functioning correctly.

