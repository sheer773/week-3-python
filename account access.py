class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(f"Account Holder: {self.name}, Balance: {self.balance}")

# Example
acc = BankAccount("Sheer", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.display_balance()