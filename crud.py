from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# In-memory "database"
books = [
    {'id': 1, 'title': "Academic", 'author': 'Guad Ran Rasom', 'publish_date': 1998},
    {'id': 2, 'title': "Nursery", 'author': 'Ram', 'publish_date': 1990},
    {'id': 3, 'title': "ACC", 'author': 'Guad', 'publish_date': 1999},
    {'id': 4, 'title': "ACAD", 'author': 'Rasom', 'publish_date': 1900},
]

app = FastAPI(title="Simple FastAPI CRUD Example")

# Pydantic model for validation
class Book(BaseModel):
    id: int
    title: str
    author: str
    publish_date: int

# -------------------- GET all books --------------------
@app.get("/")
def get_books():
    """
    Return all books in the database
    """
    return books

# -------------------- ADD a new book --------------------
@app.post("/add")
def add_book(book: Book):
    """
    Add a new book to the database
    """
    # Check for duplicate ID
    if any(b['id'] == book.id for b in books):
        raise HTTPException(status_code=400, detail=f"Book with id {book.id} already exists")
    
    books.append(book.dict())
    return {"message": "Book has been added successfully."}

# -------------------- UPDATE a book by ID --------------------
@app.put("/update/{item_id}")
def update_book(item_id: int, updated_book: Book):
    """
    Update book details by ID
    """
    for index, book in enumerate(books):
        if book['id'] == item_id:
            books[index] = updated_book.dict()
            return {"message": f"Book with id {item_id} has been updated."}
    raise HTTPException(status_code=404, detail=f"Book with id {item_id} not found.")

# -------------------- DELETE a book by ID --------------------
@app.delete("/delete/{item_id}")
def delete_book(item_id: int):
    """
    Delete a book by ID
    """
    for index, book in enumerate(books):
        if book['id'] == item_id:
            books.pop(index)
            return {"message": f"Book with id {item_id} has been deleted."}
    raise HTTPException(status_code=404, detail=f"Book with id {item_id} not found.")