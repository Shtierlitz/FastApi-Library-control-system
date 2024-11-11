# app/api/v1/endpoints/book_usage.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from crud.book_usage_service import BookUsageService
from db.session import get_db
from schemas.book_usage import BookUsageRead, BookUsageCreate

router = APIRouter()


@router.post("/", response_model=BookUsageRead, status_code=status.HTTP_201_CREATED)
def create_book_usage(book_usage: BookUsageCreate, db: Session = Depends(get_db)):
    book_usage_service = BookUsageService(db)
    return book_usage_service.create_book_usage(book_usage)


@router.put("/{book_usage_id}/return", response_model=BookUsageRead)
def return_book(book_usage_id: int, book_return_date: str, db: Session = Depends(get_db)):
    book_usage_service = BookUsageService(db)
    return book_usage_service.return_book(book_usage_id, book_return_date)


@router.get("/{book_usage_id}", response_model=BookUsageRead)
def read_book_usage(book_usage_id: int, db: Session = Depends(get_db)):
    book_usage_service = BookUsageService(db)
    db_book_usage = book_usage_service.get_book_usage_by_id(book_usage_id)
    return db_book_usage


@router.get("/", response_model=list[BookUsageRead])
def read_book_usages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    book_usage_service = BookUsageService(db)
    return book_usage_service.get_book_usages(skip=skip, limit=limit)


@router.put("/{book_usage_id}", response_model=BookUsageRead)
def update_book_usage(book_usage_id: int, book_usage: BookUsageCreate, db: Session = Depends(get_db)):
    book_usage_service = BookUsageService(db)
    updated_book_usage = book_usage_service.update_book_usage(book_usage_id, book_usage)
    return updated_book_usage


@router.delete("/{book_usage_id}", response_model=dict)
def delete_book_usage(book_usage_id: int, db: Session = Depends(get_db)):
    book_usage_service = BookUsageService(db)
    book_usage_service.delete_book_usage(book_usage_id)
    return {"message": "Book usage deleted successfully"}
