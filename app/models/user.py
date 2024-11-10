# app/models/user.py
from sqlalchemy import Column, Integer, String, DateTime, func
from db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    date_registered = Column(DateTime, server_default=func.now())
