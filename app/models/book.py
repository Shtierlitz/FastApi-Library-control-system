# app/models/book.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    genre = Column(String, index=True)
    year_published = Column(Integer)

    # Relationship with the author
    author = relationship("Author", back_populates="books")
