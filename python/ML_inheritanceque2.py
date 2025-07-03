# Create a class Account with a constructor that initializes balance.
#  Inherit a class SavingsAccount that uses super() to call the parent constructor and adds interest_rate. Print all attributes.

class Accounts:
    def __init__(self,balance):
        self.balance=balance

class SavingAccount(Accounts):
    def __init__(self,balance,interest_rate):
        super().__init__(balance)
        self.interest_rate=interest_rate

    def print_attributes(self):
        print(f"Balance:{self.balance}")
        print(f"interest_rate:{self.interest_rate}")

Saving_Accounts=SavingAccount(1000,2)

Saving_Accounts.print_attributes()
