# main.py: Esta aplicación expone un endpoint básico para consultar los registros de la tabla usuarios

import os
from fastapi import FastAPI, HTTPException
import pandas as pd
from sqlalchemy import create_engine

app = FastAPI(title="API de Usuarios", version="1.0")

# Leer variables de entorno (inyectadas por Docker)
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "db_1")
POSTGRES_USER = os.getenv("POSTGRES_USER", "admin")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "1234")

# Construir cadena de conexión para SQLAlchemy
connection_string = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
engine = create_engine(connection_string)

@app.get("/")
def read_root():
    return {"mensaje": "¡Bienvenido a la API con FastAPI y PostgreSQL!"}

@app.get("/usuarios")
def obtener_usuarios():
    try:
        query = "SELECT * FROM usuarios;"
        # Usamos pandas con el engine de SQLAlchemy
        df = pd.read_sql(query, engine)
        # Convertimos el DataFrame a una lista de diccionarios JSON
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar la base de datos: {e}")

@app.get("/usuarios/{usuario_id}")
def obtener_usuario_por_id(usuario_id: int):
    try:
        query = "SELECT * FROM usuarios WHERE id = %(val)s;"
        df = pd.read_sql(query, engine, params={"val": usuario_id})
        
        if df.empty:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
            
        return df.to_dict(orient="records")[0]
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar la base de datos: {e}")