class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder  
        self.__balance = balance                 

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    def account_type(self):
        raise NotImplementedError("Subclasses must override account_type()")


class SavingsAccount(BankAccount):
    def account_type(self):
        return "This is a Savings Account"


class CurrentAccount(BankAccount):
    def account_type(self):
        return "This is a Current Account"


# Create instances of SavingsAccount and CurrentAccount
accounts = [
    SavingsAccount("Aliana", 1500),
    CurrentAccount("Bobby", 2500)
]

# Call account_type() on each account and print account details
for account in accounts:
    print(f"{account.get_account_holder()}: {account.account_type()}, Balance: {account.get_balance()}")
