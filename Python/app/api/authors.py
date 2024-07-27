from flask import Blueprint, request, jsonify
from app.db.database import get_db
from app.crud.author import create_author, get_authors, delete_author
from sqlalchemy.orm import Session

authors_bp = Blueprint('authors', __name__)

@authors_bp.route("/authors", methods=["POST"])
def add_author():
    db: Session = next(get_db())
    name = request.json["name"]
    author = create_author(db, author_name=name)
    return jsonify({"id": author.id, "name": author.name})

@authors_bp.route("/authors", methods=["GET"])
def list_authors():
    db: Session = next(get_db())
    authors = get_authors(db)
    return jsonify([{"id": author.id, "name": author.name} for author in authors])

@authors_bp.route("/authors/<int:author_id>", methods=["DELETE"])
def remove_author(author_id: int):
    db: Session = next(get_db())
    author = delete_author(db, author_id=author_id)
    if author:
        return jsonify({"message": "Author deleted", "id": author_id})
    return jsonify({"message": "Author not found"}), 404

