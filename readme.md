## About Project

Book Management Service

# How to install

Follow SEL rules for updating the library ensuring proper git branching, test update, dependencies inclusion and code documentation and wider documentation.

To setup the library for update:

```
poetry shell # To activate environment
poetry install # To install dependencies
```

To add new dependencies:

```
poetry add {dependency_name}
poetry add {dependency_name} --group dev # To add dev dependencies
```

# How to Run the Project

After setting up the environment and installing dependencies, you can run the project with the following commands:

### Activate the Poetry Shell:
```
poetry shell
```

### Run the Application
```
uvicorn app.main:app --reload
```
This command starts the server in development mode with hot-reloading. You can then access the application locally at http://127.0.0.1:8000.

Add --port XXXX if you want to specify the port

# How to test

To run test:
```
poetry run pytest
poetry run pytest --cov # Run with coverage info
```

# More info

```
book_collection/
├── app/
│   ├── core/
│   │   ├── config.py             # Application configuration
│   │   ├── security.py           # Security utilities (JWT, hashing)
│   │   └── errors.py             # Custom error handling and exceptions
│   ├── models/
│   │   ├── user.py               # User model
│   │   └── book.py               # Book model
│   ├── routers/
│   │   ├── v1/                   # API version 1 routers
│   │   │   ├── auth_router.py    # Auth routes (signup, login)
│   │   │   └── books_router.py   # Book CRUD routes
│   ├── schemas/
│   │   ├── user.py               # User Pydantic schemas
│   │   └── book.py               # Book Pydantic schemas
│   ├── crud/
│   │   ├── user_crud.py          # CRUD functions for user
│   │   └── book_crud.py          # CRUD functions for book
│   ├── services/
│   │   ├── auth_service.py       # Handles user registration and login
│   │   └── book_service.py       # Book-related business logic
│   ├── db/
│   │   └── session.py            # Database session management
│   ├── main.py                   # Main FastAPI app
│   └── deps.py                   # Dependency functions for routes
└── tests/
    ├── test_auth.py              # Tests for authentication
    └── test_books.py             # Tests for book CRUD
``` 