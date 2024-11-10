from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.author_service import AuthorService
from db.session import get_db
from schemas.author import AuthorRead, AuthorCreate

router = APIRouter()


@router.post("/", response_model=AuthorRead)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    book_service = AuthorService(db)
    return book_service.create_author(author)


@router.get("/{author_id}", response_model=AuthorRead)
def read_author(author_id: int, db: Session = Depends(get_db)):
    book_service = AuthorService(db)
    db_author = book_service.get_author_by_id(author_id)
    return db_author


@router.get("/", response_model=list[AuthorRead])
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    book_service = AuthorService(db)
    return book_service.get_authors(skip=skip, limit=limit)


@router.put("/{author_id}", response_model=AuthorRead)
def update_author(author_id: int, author: AuthorCreate, db: Session = Depends(get_db)):
    book_service = AuthorService(db)
    updated_author = book_service.update_author(author_id, author)
    return updated_author


@router.delete("/{author_id}", response_model=dict)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    book_service = AuthorService(db)
    book_service.delete_author(author_id)
    return {"message": "Author deleted successfully"}
