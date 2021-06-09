class User:		# here's what we have so far


    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = BankAccount(name, email, int_rate = .02, balance = 0)

    # adding the deposit method

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance.deposit(amount) 
        return self


    def make_withdrawal(self, amount):
        self.account_balance.withdraw(amount) 
        return self


    def display_user_balance(self):
        print(self.account_balance.balance)
        return self

class BankAccount:

    def __init__(self, name, email, int_rate = .01, balance = 0): 
        self.name = name
        self.email = email
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("not enough money")
        else: 
            self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance = self.balance + interest
        return self
        
        #increases the account balance by the current balance * the interest rate (as long as the balance is positive)
Floyd = BankAccount('Floyd', 'thefloydmaywether@gmail.com', )
Donald = BankAccount('Donald', 'number45@gmail.com')

Harry = User('Harry', 'harrystyles@hotmail.com')
Floyd = User('Floyd', 'thefloydmaywether@gmail.com')
Donald = User('Donald', 'number45@gmail.com')

Harry.make_deposit(100).make_deposit(250).make_deposit(200).make_withdrawal(150).display_user_balance()


Floyd.make_deposit(100000000).make_deposit(420000000).make_withdrawal(10000).make_withdrawal(25000).display_user_balance()


Donald.make_deposit(200000000).make_withdrawal(200000).make_withdrawal(15000).make_withdrawal(10000).display_user_balance()