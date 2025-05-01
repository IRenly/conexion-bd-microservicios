from fastapi import FastAPI
from routes import programa_routes
from contextlib import asynccontextmanager
from database import Base, engine
import sys

# Detectamos si estamos en modo test
IS_TEST = any(arg.startswith("pytest") for arg in sys.argv)

@asynccontextmanager
async def lifespan(app: FastAPI):
    if not IS_TEST:
        # Solo crear las tablas si no estamos en modo test
        Base.metadata.create_all(bind=engine)
    yield
    # (Aquí podrías cerrar conexiones u otros recursos si hiciera falta)

app = FastAPI(lifespan=lifespan, title="Microservicio de Programas académicos")

# Incluir las rutas
app.include_router(programa_routes.router)

@app.get("/")
def home():
    return {"message": "Microservicio de Programas en funcionamiento"}
