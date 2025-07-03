class Account:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def get_balance(self):
        """Getter method to access the balance."""
        return self.__balance

    def set_balance(self, amount):
        """Setter method to update the balance, ensuring it cannot be negative."""
        if amount < 0:
            print("Balance cannot be negative!")
        else:
            self.__balance = amount

# Create an Account object
account = Account(100)

try:
    print(account.__balance)  # This will not work
except AttributeError as e:
    print(e)

# Using methods to access and modify the balance
print("Current Balance:", account.get_balance()) 

account.set_balance(200) 
print("Updated Balance:", account.get_balance()) 

account.set_balance(-50)
