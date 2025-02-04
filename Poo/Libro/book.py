from datetime import datetime

class book:
    def __init__(self, title, author, year,price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def show_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nPrice: {self.price}"
    

    def apply_discount(self, discount):
        self.price = self.price - (self.price * discount / 100)
        return self.price
    
    def is_new(self):
        current_year = datetime.now().year
        book_years = current_year - self.year
        if book_years < 2:
            return True
        else:
            return False
        


libro1= book("El principito", "Antoine de Saint-Exupéry", 2024, 1000)
print(libro1.show_info())
print(libro1.apply_discount(10))
print(libro1.is_new())


