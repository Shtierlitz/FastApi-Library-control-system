# app/schemas/user.py
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int
    date_registered: Optional[datetime] = None

    class Config:
        from_attributes = True  # Allows working with ORM objects (SQLAlchemy)
