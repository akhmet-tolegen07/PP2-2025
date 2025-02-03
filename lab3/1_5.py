class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(amount, "added to account. New balance: ", self.balance, "tg")
        else:
            print("The deposit amount must be greater than zero.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds! Available only: ", self.balance, "tg")
        elif amount > 0:
            self.balance -= amount
            print(amount, "withdrawn from the account. New balance: ", self.balance, "tg")
        else:
            print("The withdrawal amount must be greater than zero.")


acc = Account("Akhmet", 100000)

acc.deposit(20000)
acc.withdraw(35000)
acc.withdraw(300000) 
acc.withdraw(-10300)
