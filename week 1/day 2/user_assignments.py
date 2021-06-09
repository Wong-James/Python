class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    # adding the deposit method

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self


    def display_user_balance(self):
        print(self.account_balance)
        return self

Harry = User('Harry', 'harrystyles@hotmail.com')
Floyd = User('Floyd', 'thefloydmaywether@gmail.com')
Donald = User('Donald', 'number45@gmail.com')

Harry.make_deposit(100).make_deposit(250).make_deposit(200).make_withdrawal(150).display_user_balance()


Floyd.make_deposit(100000000).make_deposit(420000000).make_withdrawal(10000).make_withdrawal(25000).display_user_balance()


Donald.make_deposit(200000000).make_withdrawal(200000).make_withdrawal(15000).make_withdrawal(10000).display_user_balance()

# the specific user's account increases by the amount of the value received

