class Users:
    #Create a file with the User class, including the __init__ 
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    #make_deposit methods
    def make_deposit(self, amount):
        self.account_balance += amount

    #make_withdrawals methods
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    #Add a display_user_balance method to the User class
    def display_user_balance(self):
        print('User:', self.name, 'Balance:$', self.account_balance)

    #transfer money from one user to another
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)

#create 3 instances of users class
matthew = Users('Matthew', 'Matthew.le21@gmail.com')
alyssa = Users('Alyssa', 'Alyssa.Agabon21@gmail.com')
alex = Users('Alex', 'Alex.le@gmail.com')

#Have the first user make 3 deposits and 1 withdrawal and then display their balance
matthew.make_deposit(500)
matthew.make_deposit(500)
matthew.make_deposit(1200)
matthew.make_withdrawal(200)

print(matthew.account_balance)

matthew.display_user_balance()

matthew.transfer_money(alyssa, 100)

print(matthew.account_balance)
print(alyssa.account_balance)