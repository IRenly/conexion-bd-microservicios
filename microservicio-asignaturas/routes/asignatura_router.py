from fastapi import APIRouter, Depends
from models.asignatura_model import Asignatura
from controller import asignatura_controller
from sqlalchemy.orm import Session
from database import get_db

asignatura_router = APIRouter(prefix="/asignatura")


@asignatura_router.get('/')
async def consultar_asignaturas(db: Session = Depends(get_db)):
    # Asegurarse de pasar el db a la función del controlador
    return asignatura_controller.obtener_asignaturas(db)


@asignatura_router.get('/{id}')
async def consultar_asignatura_por_id(id: int, db: Session = Depends(get_db)):
    # Asegurarse de pasar el db a la función del controlador
    return asignatura_controller.obtener_asignatura_por_id(id, db)


@asignatura_router.post('/crear-asignatura')
async def crear_asignatura(asignatura: Asignatura, db: Session = Depends(get_db)):
    # Asegurarse de pasar el db a la función del controlador
    return await asignatura_controller.crear_asignatura(asignatura, db)


@asignatura_router.put('/actualizar-asignatura/{id}')
async def actualizar_asignatura(id: int, nueva_asignatura: Asignatura, db: Session = Depends(get_db)):
    # Asegurarse de pasar el db a la función del controlador
    return await asignatura_controller.modificar_asignatura(id, nueva_asignatura, db)


@asignatura_router.delete('/eliminar-asignatura/{id}')
async def eliminar_asignatura(id: int, db: Session = Depends(get_db)):
    # Asegurarse de pasar el db a la función del controlador
    return asignatura_controller.eliminar_asignatura(id, db)
