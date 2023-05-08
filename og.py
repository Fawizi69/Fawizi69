class Account:
    def _init_(self):
        self.name = "fawaz abdulsalam" \
                    ""
        self.account_number = 1624750089
        self.account_balance = 500000

    def deposite(self, amount):
        self.account_balance = self.account_balance + amount
        print(self.account_balance)

    def withdraw(self, amount):
        self.account_balance = self.account_balance - amount
        print(self.account_balance)
