from fastapi import FastAPI
import time
from Servicio_Saludos import servicio
from Modelo_Saludo import Saludo
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World", "FastAPI": "is running!"}

@app.get("/saludo/{nombre}")
def saludar(nombre: str, idioma: str = "español"):
   saludo=servicio.crear_saludo(nombre,idioma)
   return saludo

@app.get("/saludos", response_model=List[Saludo])
def obtener_saludos():
    return servicio.obtener_todos_saludos()
