# app/schemas/book.py

from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    genre: Optional[str] = None
    year_published: Optional[int] = None


class BookCreate(BookBase):
    author_id: int


class BookRead(BookBase):
    id: int
    author_id: int

    class Config:
        from_attributes = True  # Allows working with ORM objects (SQLAlchemy)
