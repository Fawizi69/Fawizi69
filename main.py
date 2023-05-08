from account import Account

class Current_account(Account):
    def _init_(self):
        Account._init_(self)

current = Current_account()
current.deposite(0000)
