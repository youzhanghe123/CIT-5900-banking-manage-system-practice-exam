class Account(object):
    """"A class for representing a bank account with account information and
    balance.
    """
    
    def __init__(self, account_number, first_name, last_name):
        """Initialize bank account with account number, first name, last name, 
        and a starting balance of 0.
        """
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0.0
        
    def __str__(self):
        """"Returns string representation of the account.
        Called by str(object) and the built-in functions format() and print()
        to compute an "informal" or nicely printable string representation.
        Returns account number, first name, last name, and balance rounded to 2 
        decimal places.
        """
        
        return  f"Account Number: {self.account_number}, " \
                f"First Name: {self.first_name}, " \
                f"Last Name: {self.last_name}, " \
                f"Balance: {self.balance:.2f}"