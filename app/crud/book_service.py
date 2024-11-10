# app/crud/book_service.py
from typing import List, Type, Optional

from sqlalchemy.orm import Session
from schemas.book import BookCreate
from core.exceptions import BookNotFound
from models.book import Book


class BookService:
    def __init__(self, db: Session):
        self.db = db

    def create_book(self, book: BookCreate):
        db_book = Book(**book.dict())
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return db_book

    def get_book(self, book_id: int):
        book = self.db.query(Book).filter(Book.id == book_id).first()
        if not book:
            raise BookNotFound()
        return book

    def get_books(self, skip: int = 0, limit: int = 10) -> list[Type[Book]]:
        return self.db.query(Book).offset(skip).limit(limit).all()

    def update_book(self, book_id: int, book_data: BookCreate) -> Optional[Book]:
        db_book = self.get_book(book_id)
        if db_book:
            for key, value in book_data.dict().items():
                setattr(db_book, key, value)
            self.db.commit()
            self.db.refresh(db_book)
        return db_book

    def delete_book(self, book_id: int):
        db_book = self.get_book(book_id)
        if db_book:
            self.db.delete(db_book)
            self.db.commit()
