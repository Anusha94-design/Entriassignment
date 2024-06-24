#BANKING SYSTEM PROJECT
class Bank_Account:
    def __init__(self,):
     self.balance=0
    print("HELLO!!! Welcome to Bank Of India")
    def account(self):
        name=input("Enter your  account name")
        number=int(input("Enter your account number"))
    def deposit(self):
        amount=float(input("Enter amount to be Deposited:"))
        self.balance+=amount
        print("Amount Deposited:",amount)
    def withdraw(self):
        amount=float(input("Enter amount to be withrawn:"))
        if self.balance>=amount:
            self.balance-=amount
            print("withdrew:",amount)
        else :
          print("Insufficient Balance")
    def display(self):
            print("Available Balance=",self.balance)
s=Bank_Account()
s.account()
s.deposit()
s.withdraw()
s.display()
