class BankAccount:
    def __init__(self, int_rate, balance):
        self.interest_rate = int_rate
        self.balance = balance

    def deposit(self, amount, account_type):
        self.balance += amount
        print(f"${amount} was successfully deposited into {account_type}")
        return self

    def withdrawal(self, amount, account_type):
        if self.balance >= amount:
            self.balance -= amount
            print(f"${amount} was successfully withdrawn from {account_type}")
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.amount -= 5
        return self

    def display_acct_info(self, account_type):
        print(f"{account_type} Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.amount = (self.amount * self.interest_rate) + self.amount
        return self

class Users:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.accounts = {}

    def create_account(self, account_type, amount, int_rate):
        self.accounts[account_type] = BankAccount(int_rate, amount)
        print(f"{account_type} account has been sucessfully created")
        return self


    def make_deposit(self, amount, account_type):
        if account_type in self.accounts:
            self.accounts[account_type].deposit(amount, account_type)
        else: 
            print(f"Account type '{account_type}' does not exist")
        return self

    def make_withdrawal(self, amount, account_type):
        if account_type in self.accounts:
            self.accounts[account_type].withdrawal(amount, account_type)
        else:
            print(f"Account type '{account_type}' does not exist")

        return self

    def display_user_balance(self, account_type):
        if account_type in self.accounts:
            self.accounts[account_type].display_acct_info(account_type)
        else:
            print(f"Account type '{account_type}' does not exist")
        return self


    # def transfer_money(self, other_user, amount):
    #     other_user.make_deposit(amount)
    #     self.make_withdrawal(amount)
    #     return self

matthew = Users("Matthew", "matthew.le21@gmail.com")
alyssa = Users("Alyssa", "avaagabon@gmail.com")

matthew.create_account("Checkings", 100000, .02).create_account("Savings", 500000, .10).create_account("Retirement", 1000000, .25)
matthew.make_deposit(100000, "Checkings").make_withdrawal(5000, "Savings")
matthew.display_user_balance("Checkings").display_user_balance("Savings")

