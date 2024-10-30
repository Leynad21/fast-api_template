from sqlalchemy.orm import Session
from app.schemas.book import BookCreate
from app.crud.book_crud import create_book, get_books
from fastapi import HTTPException, status


def create_user_book(db: Session, book_data: BookCreate, user_id: int):
    return create_book(db, book_data, user_id)


def get_user_books(db: Session, user_id: int):
    books = get_books(db, user_id)
    if not books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No books found for this user")
    return books
