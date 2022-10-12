
class account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance
class saving_account(account):
    def __init__(self,title,balance,rate=0):
        super().__init__(title,balance)
        self.interest_rate=rate
    def __str__(self):
        return f"title:{self.title} \nbalance:{self.balance} \ninterest_rate:{self.interest_rate}"
title=input("enter title:")
balance = input("enter balance:")
rate = input("enter rate:")
obj = saving_account(title,balance,rate)
print(obj)

