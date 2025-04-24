import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base  # Importar Base desde base.py

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:root@db:5432/asignacion_espacios")

engine = create_engine(url=DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
