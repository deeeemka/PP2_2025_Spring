class Account():
    def __init__(self , owner , balance ):
        self.owner = owner
        self.balance = balance
        print("Owner: " , self.owner)
        print("Your balance: " , self.balance)
    def deposit(self , num):
        if num >0:
            self.balance += num
        print("Your new balance is: " , self.balance)
    def withdraw(self , number):
        if number <= self.balance:
            self.balance -= number
        print("Your new balance is: " , self.balance)
owner = str(input())
balance = int(input())
answer = Account(owner , balance)
dep = int(input("How much money do you want to add: "))
answer.deposit(dep)
drop = int(input("How much money do you want to drop: "))
answer.withdraw(drop)