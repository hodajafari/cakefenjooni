class Account:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.balance=1000
    def deposit(self,amount):
        print(f"amount of deposit={amount}")
        self.balance=self.balance+amount
        print(f"amount of balance is {self.balance}")
    def withdraw(self,amount):
        if int (self.balance < amount):
            print("Not enough money")
        else:

            print(f"amount of withdraw={amount}")
            self.balance = self.balance - amount
            print(f"amount of balance is {self.balance}")
    def display(self):
        print(f"amount of balance of {self.name} ist {self.balance} $")
account=Account("John",20)
account.deposit(100)
account.withdraw(200)
account.withdraw(1500)
account.display()