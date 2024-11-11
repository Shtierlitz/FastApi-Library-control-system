# app/crud/book_usage_service.py
from __future__ import annotations

from sqlalchemy.orm import Session

from core.exceptions import BookUsageNotFound
from core.utils import parse_date
from models.book_usage import BookUsage
from schemas.book_usage import BookUsageCreate


class BookUsageService:
    def __init__(self, db: Session):
        self.db = db

    def create_book_usage(self, book_usage_data: BookUsageCreate) -> BookUsage:
        date_borrowed = parse_date(book_usage_data.date_borrowed)
        date_returned = parse_date(book_usage_data.date_returned)
        due_date = parse_date(book_usage_data.due_date)

        db_book_usage = BookUsage(
            user_id=book_usage_data.user_id,
            book_id=book_usage_data.book_id,
            date_borrowed=date_borrowed,
            date_returned=date_returned,
            due_date=due_date
        )

        self.db.add(db_book_usage)
        self.db.commit()
        self.db.refresh(db_book_usage)
        return db_book_usage

    def return_book(self, book_usage_id: int, book_return_date: str):
        db_book_usage = self.get_book_usage_by_id(book_usage_id)
        db_book_usage.date_returned = parse_date(book_return_date)
        self.db.commit()
        self.db.refresh(db_book_usage)
        return db_book_usage

    def get_book_usage_by_id(self, book_usage_id: int) -> BookUsage:
        book_usage = self.db.query(BookUsage).filter(BookUsage.id == book_usage_id).first()
        if not book_usage:
            raise BookUsageNotFound()
        return book_usage

    def get_book_usages(self, skip: int = 0, limit: int = 10):
        return self.db.query(BookUsage).offset(skip).limit(limit).all()

    def update_book_usage(self, book_usage_id: int, book_usage_data: BookUsageCreate):
        db_book_usage = self.get_book_usage_by_id(book_usage_id)
        for key, value in book_usage_data.dict().items():
            setattr(db_book_usage, key, value)
        self.db.commit()
        self.db.refresh(db_book_usage)
        return db_book_usage

    def delete_book_usage(self, book_usage_id: int):
        db_book_usage = self.get_book_usage_by_id(book_usage_id)
        self.db.delete(db_book_usage)
        self.db.commit()
        return {"message": "Book usage deleted successfully"}
