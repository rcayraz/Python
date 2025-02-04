class AccountBanck:
    def __init__(self, name, balance_init):
        self.name = name
        self.__balance = balance_init

    def get_balance(self):
        return self.__balance
    
    def deposit(self,cant):
        if cant > 0:
            self.__balance += cant
            
        else:
            print("Cant deposit negative amount")

    def withdraw(self,cant):
        if 0 < cant <= self.__balance:
            self.__balance -= cant
        else:
            print("Cant withdraw negative amount or more than balance")



account1= AccountBanck("John", 1000)
print(account1.get_balance())
account1.deposit(500)
print(account1.get_balance())
account1.withdraw(2500)

account2= AccountBanck("Mary", 2000)
print(account2.get_balance())
account2.deposit(500)
print(account2.get_balance())
account2.withdraw(200)
