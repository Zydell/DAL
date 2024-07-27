from flask import Blueprint, request, jsonify
from app.db.database import get_db
from app.crud.book import create_book, get_books, delete_book
from sqlalchemy.orm import Session

books_bp = Blueprint('books', __name__)

@books_bp.route("/books", methods=["POST"])
def add_book():
    db: Session = next(get_db())
    title = request.json["title"]
    author_id = request.json["author_id"]
    book = create_book(db, title=title, author_id=author_id)
    return jsonify({"id": book.id, "title": book.title, "author_id": book.author_id})

@books_bp.route("/books", methods=["GET"])
def list_books():
    db: Session = next(get_db())
    books = get_books(db)
    return jsonify([{"id": book.id, "title": book.title, "author_id": book.author_id} for book in books])

@books_bp.route("/books/<int:book_id>", methods=["DELETE"])
def remove_book(book_id: int):
    db: Session = next(get_db())
    book = delete_book(db, book_id=book_id)
    if book:
        return jsonify({"message": "Book deleted", "id": book_id})
    return jsonify({"message": "Book not found"}), 404
