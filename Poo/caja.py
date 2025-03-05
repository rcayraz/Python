class Caja :
    def __init__(self):
        self.contend=" cosas valiosas"

    def mostrar_contenido(self):
        return f"La caja contiene: {self.contend}"
    def _abrir(self):
        return "Caja abierta"
    
    def __cerrar(self):
        return "Caja cerrada"    
    
    def acceder(self):
        self._abrir()
        self.mostrar_contenido()
        self.__cerrar()



caja1 = Caja()
print(caja1.acceder())