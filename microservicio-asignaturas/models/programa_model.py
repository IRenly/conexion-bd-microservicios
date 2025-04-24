from sqlalchemy import Column, Integer, String
from base import Base  # Importar Base desde base.py
from sqlalchemy.orm import relationship

  # opcional, solo necesario si usas con anotaciones

class Programa(Base):
    __tablename__ = "programas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False, index=True)
    descripcion = Column(String, nullable=True)
    codigo_programa = Column(String(4), nullable=False, unique=True)

    asignaturas = relationship("AsignaturaDB", back_populates="programa")

