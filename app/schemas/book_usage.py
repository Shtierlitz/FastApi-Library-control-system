# app/schemas/book_usage_service.py
from datetime import datetime

from pydantic import BaseModel


class BookUsageBase(BaseModel):
    user_id: int
    book_id: int
    date_borrowed: datetime
    date_returned: datetime = None
    due_date: datetime


class BookUsageCreate(BookUsageBase):
    pass


class BookUsageRead(BookUsageBase):
    id: int

    class Config:
        from_attributes = True
