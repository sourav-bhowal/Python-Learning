class Account:
    def __init__(self, accountNo, balance = 0):
        self.accountNo = accountNo
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Money not available")

    def calculateInterest(self, interestRate):
        self.balance = self.balance + (self.balance * interestRate)
        return self.balance



class SavingsAccount(Account):
    def __init__(self, accountNo, balance=0, interestRate = 0.05):
        super().__init__(accountNo, balance)
        self.interestRate = interestRate

    def calculateInterest(self):
        return super().calculateInterest(self.interestRate)



class CurrentAccount(Account):
    def __init__(self, accountNo, balance=0, overDraftLimit = 200):
        super().__init__(accountNo, balance)
        self.overDraftLimit = overDraftLimit

    def withdraw(self, amount):
        if amount <= self.balance + self.overDraftLimit:
            self.balance -= amount
        else:
            print("Exceeds overDraft Limit.")


x = SavingsAccount("A01", 1000)
x.deposit(1000)
x.withdraw(500)

print(x.balance)
print(x.calculateInterest())
###############################################################

y = CurrentAccount("A01", 1000)
y.deposit(1000)
y.withdraw(2100)

print(y.balance)