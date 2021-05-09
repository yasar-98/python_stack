class Bank_account:
    def __init__(self,accont_balance=0, interest_rate=0.01):
        self.accont_balance=accont_balance
        self.interest_rate=interest_rate
    def deposit(self, amount):
        self.accont_balance+=amount
        return self
    def make_withdrawal(self, amount=0):
        if amount<=self.accont_balance:
            self.accont_balance-=amount
        else:
            self.accont_balance-=5
            print("Insufficient funds: Charging a $5 fee")
        return self
    def display_account_info(self): 
        print(f"the balance is {self.accont_balance}")
        return self

    def yield_interest(self):
        if self.accont_balance>0:
            self.accont_balance+=self.interest_rate*self.accont_balance
        return self

x=Bank_account(400)
x.display_account_info().make_withdrawal(100).display_account_info().deposit(100).display_account_info().yield_interest().display_account_info()

