class Account:
    def __init__(self, initial_amount):
        self.__amount = initial_amount


    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, new_amount):
        if new_amount < 0:
            print("The amount can't be negative")
            self.__amount = 0
        else:
            self.__amount = new_amount    


account1 = Account(1000)
print(account1.amount)
account1.amount = -1000
print(account1.amount)
account1.amount = 500
