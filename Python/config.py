import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:123321@localhost/db_dal_python")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
