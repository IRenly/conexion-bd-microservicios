# schemas/asignatura_schema.py
from pydantic import BaseModel

class AsignaturaBase(BaseModel):
    nombre: str
    programa_id: int

class Asignatura(AsignaturaBase):
    id: int

    class Config:
        orm_mode = True  # Permite convertir objetos SQLAlchemy en objetos Pydantic
