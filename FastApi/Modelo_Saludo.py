from fastapi import FastAPI
from  pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from enum import Enum

class Saludo(BaseModel):
    nombre : str
    mensaje: str = Field(..., description="Mensaje de saludo personalizado")
    idioma: str = "español" 
    fecha: datetime

app = FastAPI()
