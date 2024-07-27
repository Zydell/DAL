from sqlalchemy.orm import Session
from app.models.book import Book

def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Book).offset(skip).limit(limit).all()

def create_book(db: Session, title: str, author_id: int):
    db_book = Book(title=title, author_id=author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book:
        db.delete(book)
        db.commit()
        return book
    return None
