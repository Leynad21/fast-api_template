from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate


def create_book(db: Session, book: BookCreate, user_id: int):
    db_book = Book(**book.dict(), owner_id=user_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session, user_id: int):
    return db.query(Book).filter(Book.owner_id == user_id).all()


def get_book(db: Session, book_id: int, user_id: int):
    return db.query(Book).filter(Book.id == book_id, Book.owner_id == user_id).first()


def update_book(db: Session, book_id: int, book_data: BookUpdate, user_id: int):
    db_book = get_book(db, book_id, user_id)
    if db_book:
        for key, value in book_data.dict(exclude_unset=True).items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int, user_id: int):
    db_book = get_book(db, book_id, user_id)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book
