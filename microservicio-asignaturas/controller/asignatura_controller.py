import httpx
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.asignatura_model import AsignaturaDB, Asignatura

PROGRAMAS_URL = "http://ms-programas:8001/programas"  # URL de tu microservicio de programas

# Función para verificar si el programa existe
async def verificar_programa_existe(programa_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PROGRAMAS_URL}/{programa_id}")
        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"El programa con ID {programa_id} no existe en el microservicio de programas."
            )

def obtener_asignaturas(db: Session):
    return db.query(AsignaturaDB).all()

def obtener_asignatura_por_id(id: int, db: Session):
    asignatura = db.query(AsignaturaDB).filter(AsignaturaDB.id == id).first()
    if not asignatura:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La asignatura con ID {id} no fue encontrada.")
    return asignatura

async def crear_asignatura(asignatura: Asignatura, db: Session):
    # Verificar si el programa existe antes de crear la asignatura
    await verificar_programa_existe(asignatura.programa_id)

    if db.query(AsignaturaDB).filter(AsignaturaDB.nombre == asignatura.nombre).first():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"La asignatura {asignatura.nombre} ya existe.")
    
    nueva_asignatura = AsignaturaDB(
        nombre=asignatura.nombre,
        programa_id=asignatura.programa_id
    )
    db.add(nueva_asignatura)
    db.commit()
    db.refresh(nueva_asignatura)
    return nueva_asignatura

async def modificar_asignatura(id: int, asignatura: Asignatura, db: Session):
    asignatura_db = db.query(AsignaturaDB).filter(AsignaturaDB.id == id).first()
    if not asignatura_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La asignatura con ID {id} no fue encontrada.")
    
    # Verificar si el programa asociado al ID existe
    await verificar_programa_existe(asignatura.programa_id)

    asignatura_db.nombre = asignatura.nombre
    asignatura_db.programa_id = asignatura.programa_id
    db.commit()
    db.refresh(asignatura_db)
    return asignatura_db

def eliminar_asignatura(id: int, db: Session):
    asignatura_db = db.query(AsignaturaDB).filter(AsignaturaDB.id == id).first()
    if not asignatura_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"La asignatura con ID {id} no fue encontrada.")
    db.delete(asignatura_db)
    db.commit()
    return {"message": f"La asignatura con ID {id} ha sido eliminada."}
