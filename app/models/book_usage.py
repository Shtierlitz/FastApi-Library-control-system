# app/models/book_usage_service.py

from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.base import Base


class BookUsage(Base):
    __tablename__ = "book_usages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    date_borrowed = Column(DateTime, default=func.now())
    due_date = Column(DateTime, nullable=False)
    date_returned = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="book_usages")
    book = relationship("Book", back_populates="book_usages")
