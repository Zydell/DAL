from app.main import app
from app.db.database import Base, engine

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    app.run()

