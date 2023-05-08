from Account import Account

class Savings_account(Account):

    def _init_(self):
        Account._init_(self)
        self.interest = 100000
        self.withdraw_limit = 250000

    def withdraw(self, amount):
        if amount < self.withdraw_limit:
            self.account_balance = self.account_balance - amount
            print(self.account_balance)
        else:
            print("The amonut is more than the withdrawal limit")
save = Savings_account()
save.withdraw(20000)