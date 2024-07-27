from flask import Flask
from app.api import authors_bp, books_bp

app = Flask(__name__)

app.register_blueprint(authors_bp)
app.register_blueprint(books_bp)

if __name__ == "__main__":
    app.run(debug=True)

