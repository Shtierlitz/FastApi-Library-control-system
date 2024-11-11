# app/api/v1/endpoints/book.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from crud.book_service import BookService
from db.session import get_db
from schemas.book import BookCreate, BookRead

router = APIRouter()


@router.post("/", response_model=BookRead, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    book_service = BookService(db)
    return book_service.create_book(book)


@router.get("/{book_id}", response_model=BookRead)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book_service = BookService(db)
    db_book = book_service.get_book_by_id(book_id)
    return db_book


@router.get("/", response_model=list[BookRead])
def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    book_service = BookService(db)
    return book_service.get_books(skip=skip, limit=limit)


@router.put("/{book_id}", response_model=BookRead)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    book_service = BookService(db)
    updated_book = book_service.update_book(book_id, book)
    return updated_book


@router.delete("/{book_id}", response_model=dict)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_service = BookService(db)
    book_service.delete_book(book_id)
    return {"message": "Book deleted successfully"}
