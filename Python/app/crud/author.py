from sqlalchemy.orm import Session
from app.models.author import Author
from app.models.book import Book

def get_author(db: Session, author_id: int):
    return db.query(Author).filter(Author.id == author_id).first()

def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Author).offset(skip).limit(limit).all()

def create_author(db: Session, author_name: str):
    db_author = Author(name=author_name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def delete_author(db: Session, author_id: int):
    author = db.query(Author).filter(Author.id == author_id).first()
    if author:
        # Eliminar libros asociados
        db.query(Book).filter(Book.author_id == author_id).delete()
        db.delete(author)
        db.commit()
        return author
    return None


