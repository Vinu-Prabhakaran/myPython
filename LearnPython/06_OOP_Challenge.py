

class BankAccount:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Bank Account owned by {self.owner} has a balance of {self.balance}'

    def __del__(self):
        return f'Bank Account owned by {self.owner} is closed!'

    def deposit(self,amount):
        self.balance += amount
        print(f'Amount of {amount} deposited. Balance is {self.balance}')

    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Amount of {amount} withdrawn . Balance is {self.balance}')
        else:
            print(f'Not enough balance!')

if __name__ == '__main__':
    acct = BankAccount("Vinu",1200)
    acct.deposit(250)
    acct.withdraw(100)
    acct.withdraw(2000)
    print(acct)
