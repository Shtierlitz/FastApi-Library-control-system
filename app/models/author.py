# app/models/author.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    birth_date = Column(String)  # Replace with Date if needed
    country = Column(String)

    # Relationship with books
    books = relationship("Book", back_populates="author")
