class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
        
    def ladrar(self):
        print(f'Guau guau, soy {self.nombre} y soy un {self.raza}')

    @classmethod
    def crear_perro(cls, nombre, raza):
        return cls(nombre, raza)
    
    @staticmethod
    def ladrar_estatico():
        print('Guau guau')


Perro1 = Perro('Firulais', 'Pastor Aleman')
Perro1.ladrar()
Perro2 = Perro.crear_perro('Boby', 'Chihuahua')
Perro2.ladrar()
Perro.ladrar_estatico()        