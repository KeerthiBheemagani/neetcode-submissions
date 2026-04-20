class BankAccount:
    def __init__(self, balance: int): 
        self.__balance = balance # Don't modify this line

    @property    
    def get_balance(self) -> int: # TODO: Convert this method to use the @property decorator
        return self.__balance

    @get_balance.setter    
    def set_balance(self, value: int) -> None: # TODO: Convert this method to use the @property decorator
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative!")


# Don't modify the code below this line
account = BankAccount(1000)
print(account.get_balance)
account.set_balance = -100
