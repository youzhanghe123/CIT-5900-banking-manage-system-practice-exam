from Account import *
from AccountManager import *

class AccountCreator(object):
    """"A class for loading bank account information from a file, storing it in a dictionary,
    and calculating the account balance.
    """
    
    # We do not have an __init__ function and will call the default constructor.
    
    def init_bank_accounts(self, accounts, deposits, withdrawals):
        '''
        Loads the given 3 files, stores the information for individual bank accounts in a dictionary,
        and calculates the account balance. This function calculates the total balance for each account by taking the 
        total deposit amount and subtracting the total withdrawal amount.
        

        Step 1:
        For the Accounts file, get the information and put it in a bank_accounts dictionary.
        The keys for the dictionary are account numbers as strings, and the values are Account objects
        (objects of the Account class that represent individual bank accounts).
        
        Accounts file contains information about bank accounts.
        Each row contains an account number, a first name, and a last name, separated by vertical pipe (|).
        Example:
        1|Brandon|Krakowsky
        
        Step 2:
        For the Deposits file, deposit the given amounts to the given accounts. The accounts to which you're
        depositing are found in the bank_accounts dictionary you created in Step 1.
        
        Deposits file contains a list of deposits for a given account number.
        Each row contains an account number, and a list of deposit amounts, separated by a comma (,).
        Example:
        1,234.5,6352.89,1,97.60


        Step 3:
        For the Withdrawals file, withdraw the given amounts from the given accounts. The accounts from which
        you're withdrawing are found in the bank_accounts dictionary you created in step 1.
        
        Withdrawals file contains a list of withdrawals for a given account number.
        Each row contains an account number, and a list of withdrawal amounts, separated by a comma (,).
        Example:
        1,56.3,72.1
        '''
        

        bank_accounts = {}

        # TODO insert your code
        with open (accounts, "r") as f:
            for line in f:
                line=line.strip()
                line_lis=line.split("|")
                line_lis=[element.strip() for element in line_lis]
                account_number, first_name, last_name=line_lis[0],line_lis[1], line_lis[2]
                bank_accounts[account_number]=Account(account_number, first_name, last_name)
        # Now we create a dictionary with each element as a account object which is bank_accounts
        
        account_manager = AccountManager()
        
        with open(deposits,"r") as f:
            for line in f:
                line=line.strip()
                line_lis=line.split(",")
                account_number=line_lis[0]
                if len(line_lis)>1:
                    line_lis=line_lis[1:]
                    line_lis=[float(element) for element in line_lis]
                    amount=sum(line_lis)
                    account_manager.deposit(bank_accounts, account_number, amount)
                else:
                    account_manager.deposit(bank_accounts, account_number, 0)
        
        with open(withdrawals,"r") as f:
            for line in f:
                line=line.strip()
                line_lis=line.split(",")
                account_number=line_lis[0]
                if len(line_lis)>1:
                    line_lis=line_lis[1:]
                    line_lis=[float(element) for element in line_lis]
                    amount=sum(line_lis)
                    account_manager.withdraw(bank_accounts, account_number, amount)
                else:
                    account_manager.withdraw(bank_accounts, account_number, 0)
        
        

        return bank_accounts