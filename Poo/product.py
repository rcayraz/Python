class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__discount = 0


    def show_inf(self):
        return f'{self.name} costs {self.price}'
    
    def apply_discount(self,porsent):
        if 0 < porsent <= 100:
            self.__discount = porsent
            self.price = self.price - (self.price * porsent / 100)
            return self.price
        else :
            return "Invalid discount"
        
product1 = Product("Laptop", 1000)
print(product1)
print(product1.show_inf())
print(product1.apply_discount(50))
