from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.book import BookCreate, BookOut, BookUpdate
from app.crud.book_crud import create_book, get_books, get_book, update_book, delete_book
from app.deps import get_current_user, get_db
from app.models.user import User

router = APIRouter()


@router.post("/", response_model=BookOut)
def create_new_book(book: BookCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_book(db, book, current_user.id)


@router.get("/", response_model=list[BookOut])
def read_books(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_books(db, current_user.id)


@router.get("/{book_id}", response_model=BookOut)
def read_book(book_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_book = get_book(db, book_id, current_user.id)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return db_book


@router.patch("/{book_id}", response_model=BookOut)
def update_existing_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_book = update_book(db, book_id, book, current_user.id)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return db_book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_book(book_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_book = delete_book(db, book_id, current_user.id)
    if not db_book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return {"detail": "Book deleted successfully"}
