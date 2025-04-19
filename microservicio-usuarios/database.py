import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Usamos la misma base de datos para todos
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:root@db:5432/asignacion_espacios")

engine = create_engine(url=DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()