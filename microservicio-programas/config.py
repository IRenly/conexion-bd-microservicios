import os
from dotenv import load_dotenv

load_dotenv()

# Detectar si estamos ejecutando pruebas (por ejemplo, usando pytest)
IS_TEST = any(arg.startswith("pytest") for arg in os.sys.argv)

if IS_TEST:
    DATABASE_URL = "sqlite:///./test.db"
else:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:root@db:5432/asignacion_espacios")

print("Using DATABASE_URL:", DATABASE_URL)
