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

Jim.deposit(100).deposit(500).deposit(1000).withdraw(300).yield_interest().display_account_info()

Donald.deposit(1000).deposit(12000).withdraw(1000).withdraw(500).withdraw(100).withdraw(200).yield_interest().display_account_info()