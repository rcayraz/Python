
from Modelo_Saludo import Saludo
from datetime import datetime
class ServicioSaludo:
    def __init__(self):
        
        self.saludos_guardados=[]
        self.idiomas ={
            "español": "¡Hola, {}!",
            "ingles": "Hello, {}!",
            "frances": "Bonjour, {}!",
            "aleman": "Hallo, {}!"
        }

    def crear_saludo(self, nombre: str, idioma: str = "español") -> Saludo:
        mensaje = self.idiomas.get(idioma, self.idiomas["español"]).format(nombre)
        saludo = Saludo(nombre=nombre, mensaje=mensaje, idioma=idioma, fecha=datetime.now())
        self.saludos_guardados.append(saludo)
        return saludo

    def obtener_todos_saludos(self):
        """Obtiene todos los saludos guardados"""
        return self.saludos_guardados   

servicio = ServicioSaludo()
