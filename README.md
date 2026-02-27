# FastAPI CRUD Example

A simple **FastAPI CRUD API** using an in-memory list as a database.  
Perfect for learning FastAPI and building REST APIs in Python.

---

## Features

- **GET** `/` - Fetch all books
- **POST** `/add` - Add a new book
- **PUT** `/update/{item_id}` - Update a book by ID
- **DELETE** `/delete/{item_id}` - Remove a book by ID
- **Pydantic models** for data validation
- **Swagger UI** documentation included
- Clear error handling

---

## Example Data

```json
[
    {"id": 1, "title": "Academic", "author": "Guad Ran Rasom", "publish_date": 1998},
    {"id": 2, "title": "Nursery", "author": "Ram", "publish_date": 1990}
]