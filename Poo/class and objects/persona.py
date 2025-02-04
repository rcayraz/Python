class Persona():
    # Constructor de la clase
    def __init__(self, nombre, edad,direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def saludar(self):
        print(f'Hola, me llamo {self.nombre} y tengo {self.edad} años')
    
    def validar_edad(self):
        if self.edad >= 18:
            print(f'{self.nombre} es mayor de edad')
        else:
            print(f'{self.nombre} es menor de edad')




persona1 = Persona('Juan', 17, 'Calle 123')
persona1.saludar()
persona1.validar_edad()
persona2 = Persona('Karla', 30, 'Calle 456')
persona2.saludar()
persona2.validar_edad()
persona3 = Persona('Laura', 25, 'Calle 789')
persona3.saludar()
persona3.validar_edad()       