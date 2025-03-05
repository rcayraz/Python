class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    @property
    def area(self):
        return self.base * self.altura
    
    @property
    def perimetro(self):
        return 2 * (self.base + self.altura)
    


mi_rectangulo1 = Rectangulo(3, 4)
print(f"Area:{mi_rectangulo1.area}")
print(mi_rectangulo1.perimetro)
mi_rectangulo2 = Rectangulo(5, 6)
print(mi_rectangulo2.area)
print(mi_rectangulo2.perimetro)