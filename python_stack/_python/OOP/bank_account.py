class BankAccount:
    def __init__(self, int_rate, balance):
        self.interest_rate = int_rate
        self.balance = balance

    def make_deposit(self, amount):
        self.balance += amount
        return self

    def make_withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_acct_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance = (self.balance * self.interest_rate) + self.balance
        return self

account1 = BankAccount(.05, 100)
account2 = BankAccount(.10, 100)

account1.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(100).yield_interest().display_acct_info()
account2.make_deposit(100).make_deposit(200).make_withdrawal(200).make_withdrawal(300).yield_interest().display_acct_info()