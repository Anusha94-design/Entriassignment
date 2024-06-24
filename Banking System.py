#BANKING SYSTEM PROJECT
class Bank_Account:
    def __init__(self):
     self.balance=0
    print("HELLO!!! Welcome to Bank Of India")
    def login(self):
        username=input("Enter your Username")
        password=input("Enter your password")
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
s.login()
s.deposit()
s.withdraw()
s.display()
