# app/schemas/author.py

from typing import Optional

from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str
    birth_date: Optional[str] = None
    country: Optional[str] = None


class AuthorCreate(AuthorBase):
    pass


class AuthorRead(AuthorBase):
    id: int

    class Config:
        from_attributes = True  # Allows working with ORM objects (SQLAlchemy)
