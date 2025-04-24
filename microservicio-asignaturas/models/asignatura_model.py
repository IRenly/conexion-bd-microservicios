from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from base import Base  # Importar Base desde base.py
#from models.programa_model import Programa  # Importar Programa
from pydantic import BaseModel  # Importar BaseModel desde pydantic

class Asignatura(BaseModel):
    id: int
    nombre: str
    programa_id: int

    class Config:
        orm_mode = True

class AsignaturaDB(Base):
    __tablename__ = "asignaturas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    programa_id = Column(Integer, ForeignKey("programas.id"), nullable=False)

    programa = relationship("Programa", back_populates="asignaturas")
