from typing import List, Type, Optional

from sqlalchemy.orm import Session

from core.exceptions import UserNotFound, UserWithEmailAlreadyExists
from models.user import User
from schemas.user import UserCreate


class UserService:

    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, user_id: int) -> User:
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise UserNotFound()
        return user

    def get_users(self, skip: int = 0, limit: int = 10) -> List[Type[User]]:
        return self.db.query(User).offset(skip).limit(limit).all()

    def validate_email(self, email: str):
        email = self.db.query(User).filter(User.email == email).first()
        if email:
            raise UserWithEmailAlreadyExists()

    def create_user(self, user: UserCreate) -> User:
        self.validate_email(user.email)
        db_user = User(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update_user(self, user_id: int, user_data: UserCreate) -> Optional[User]:
        db_user = self.get_user_by_id(user_id)
        for key, value in user_data.dict().items():
            setattr(db_user, key, value)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def delete_user(self, user_id: int):
        db_user = self.get_user_by_id(user_id)
        self.db.delete(db_user)
        self.db.commit()
