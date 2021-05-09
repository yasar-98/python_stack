from bank_account import Bank_account
class user:
    def __init__(self,user_balance,user_name):
        self.user_name=user_name
        self.account=Bank_account()
    def deposit(self, amount):
        self.account.deposit(amount)       
    def make_withdrawal(self, amount=0):
            self.account.make_withdrawal()
    def display_user_balance(self): 
        self.account.display_account_info()
    def transfer_money(self, other_user, amount):
        happend = self.make_withdrawal(amount)
        if happend == True:
            other_user.deposit(amount)



anas=user(400,"Anas")
anas.make_withdrawal(100)
anas.deposit(100)
anas.display_user_balance()

tasneem = user(2500, "Tasneem")

print("_" * 30)
anas.display_user_balance()
tasneem.display_user_balance()
print("_" * 30)

tasneem.transfer_money(anas, 500)

anas.display_user_balance()
tasneem.display_user_balance()
