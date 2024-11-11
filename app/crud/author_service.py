from typing import List, Type, Optional

from sqlalchemy.orm import Session

from core.exceptions import AuthorNotFound
from models.author import Author
from schemas.author import AuthorCreate


class AuthorService:

    def __init__(self, db: Session):
        self.db = db

    def get_author_by_id(self, author_id: int) -> Author:
        author = self.db.query(Author).filter(Author.id == author_id).first()
        if not author:
            raise AuthorNotFound()
        return author

    def get_authors(self, skip: int = 0, limit: int = 10) -> List[Type[Author]]:
        return self.db.query(Author).offset(skip).limit(limit).all()

    def create_author(self, author: AuthorCreate) -> Author:
        db_author = Author(**author.dict())
        self.db.add(db_author)
        self.db.commit()
        self.db.refresh(db_author)
        return db_author

    def update_author(self, author_id: int, author_data: AuthorCreate) -> Optional[Author]:
        db_author = self.get_author_by_id(author_id)
        for key, value in author_data.dict().items():
            setattr(db_author, key, value)
        self.db.commit()
        self.db.refresh(db_author)
        return db_author

    def delete_author(self, author_id: int):
        db_author = self.get_author_by_id(author_id)
        self.db.delete(db_author)
        self.db.commit()
