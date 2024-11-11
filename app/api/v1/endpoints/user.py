from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from crud.user_service import UserService
from db.session import get_db
from schemas.user import UserRead, UserCreate

router = APIRouter()


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    book_service = UserService(db)
    return book_service.create_user(user)


@router.get("/{user_id}", response_model=UserRead)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    book_service = UserService(db)
    db_user = book_service.get_user_by_id(user_id)
    return db_user


@router.get("/", response_model=list[UserRead])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    book_service = UserService(db)
    return book_service.get_users(skip=skip, limit=limit)


@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    book_service = UserService(db)
    updated_user = book_service.update_user(user_id, user)
    return updated_user


@router.delete("/{user_id}", response_model=dict)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    book_service = UserService(db)
    book_service.delete_user(user_id)
    return {"message": "User deleted successfully"}
