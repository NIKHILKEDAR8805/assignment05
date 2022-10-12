class Account:
    
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate
            
    def interestAmount(self):
        interest_amount = self.interestRate * self.balance / 100
        return interest_amount

    def __str__(self):
        return f"title: {self.title}  \nbalance: {self.balance}  \ninterest rate: nikhil{self.interestRate} "

title=input('enter title:')
balance=float(input('enter balance:'))
interestRate=float(input('enter interest rate:'))
amount = float(input("enter amount:"))    

obj_account= SavingsAccount(title,balance,interestRate)

print(obj_account.__str__())

obj_account.withdrawal(amount)
print('balance after withdrawal:',obj_account.getBalance())

obj_account.deposit(amount)
print('balance after deposit:',obj_account.getBalance())

print('interest amount:',obj_account.interestAmount())
