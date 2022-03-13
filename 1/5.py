class Acc:
    def __init__(self,name, balance = 0):
        self.name = name
        self.balance = balance
    
    def withdraw(self, money):
        if (money > self.balance):
            print(self.name, "sende aksha zhetpeidi(((")
        else:
            self.balance -= money
            print("Krasavchik!")
    
    def deposit(self, money):
        self.balance += money
