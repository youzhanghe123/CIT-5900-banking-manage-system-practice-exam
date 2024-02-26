from Account import *


class AccountManager(object):
    """"A class for managing account operations.
    """
    
    # We do not have an __init__ function and will call the default constructor.
    
    def round_balance(self, bank_accounts, account_number):
        '''Rounds the given amount to two decimal places.
        '''
        #The return is an Account object
        # TODO insert your code
        bank_accounts[account_number].balance=round(bank_accounts[account_number].balance,2)
        

    def get_account(self, bank_accounts, account_number):
        '''Returns the Account object for the given account_number.
        If the account doesn't exist, returns None
        '''

        # TODO insert your code
        if account_number in list(bank_accounts.keys()):
            return bank_accounts[account_number]
        else:
            return None
        

    def withdraw(self, bank_accounts, account_number, amount):
        '''Withdraws the given amount from the account with the given account_number.
        Rounds the new balance to 2 decimal places.
        If the account doesn't exist, prints a friendly message.
        Raises a RuntimeError if the given amount is greater than the available balance.
        Prints the new balance.
        '''
        # TODO insert your code
        if self.get_account(bank_accounts, account_number)!=None: 
            if bank_accounts[account_number].balance>=amount:
                bank_accounts[account_number].balance-=amount
                self.round_balance(bank_accounts, account_number)
                print(f'New balance after withdraw:  {bank_accounts[account_number].balance}')
            else:
                raise(RuntimeError)
        else:
            print("The account does not exist")

    def deposit(self, bank_accounts, account_number, amount):
        '''Deposits the given amount into the account with the given account_number.
        Rounds the new balance to 2 decimal places.
        If the account doesn't exist, prints a friendly message.
        Prints the new balance.
        '''

        # TODO insert your code
        if self.get_account(bank_accounts, account_number)!=None:
            #print("debug ", bank_accounts[account_number].balance, "amount ",amount)
            bank_accounts[account_number].balance+=amount
            #print("debug 2 ", bank_accounts[account_number].balance)
            self.round_balance(bank_accounts, account_number)
            #print("debug 3 ", type(bank_accounts[account_number].balance))
            print(f'New balance after deposit:  {bank_accounts[account_number].balance}')
        else:
            print("The account does not exist")

    def purchase(self, bank_accounts, account_number, amounts):
        '''Makes a purchase with the total of the given amounts from the account with the given account_number.
        If the account doesn't exist, prints a friendly message.
        Calculates the total purchase amount based on the sum of the given amounts, plus (6%) sales tax.
        Raises a RuntimeError if the total purchase amount is greater than the available balance.
        Prints the new balance.
        '''

        # TODO insert your code
        total_cost=sum(amounts)*(1+0.06)
        account=self.get_account(bank_accounts, account_number)
        if account!=None:
            if account.balance>=total_cost:
                account.balance-=total_cost
            else:
                raise(RuntimeError)
        else:
            print('The account does not exist')
        

    @staticmethod
    def calculate_sales_tax(amount):
        '''Calculates and returns a 6% sales tax for the given amount.'''

        # TODO insert your code
        return amount*(1+0.06)

    def sort_accounts(self, bank_accounts, sort_type, sort_direction):
        '''Orders the bank_accounts dictionary based on the specified sort_type
        and sort_direction. Returns the sorted dictionary.
        
        If the sort_type argument is the string 'account_number', sorts based on
        the account number (e.g. '3', '5') in the given sort_direction (e.g.
        'asc', 'desc').
        Example sorted results based on account_number in ascending order:
        Account Number: 1, First Name: Brandon, Last Name: Krakowsky, Balance: 6557.59
        Account Number: 2, First Name: Chenyun, Last Name: Wei, Balance: 4716.89
        Account Number: 3, First Name: Dingyi, Last Name: Shen, Balance: 4.14
        
        Otherwise, if the sort_type argument is 'first_name', 'last_name' or
        'balance', sorts based on the associated values (e.g. 'Brandon',
        'Krakowsky', 6557.59) in the given sort direction (e.g. 'asc' or 'desc')
        Example sorted results based on 'balance' in descending order:
        Account Number: 6, First Name: Karishma, Last Name: Jain, Balance: 6700.19
        Account Number: 1, First Name: Brandon, Last Name: Krakowsky, Balance: 6557.59
        Account Number: 2, First Name: Chenyun, Last Name: Wei, Balance: 4716.89
        '''

        # TODO insert your code
        if sort_type=="account_number":
            if sort_direction=="asc":
                return {key: bank_accounts[key] for key in sorted(bank_accounts)}
            else:
                return {key: bank_accounts[key] for key in sorted(bank_accounts,reverse=True)}
        elif sort_type=="first_name":
            if sort_direction=="asc":
                return {key: value for key, value in sorted(bank_accounts.items(), key=lambda item: item[1].first_name)}
            else:
                return {key: value for key, value in sorted(bank_accounts.items(), key=lambda item: item[1].first_name,reverse=True)}
        elif sort_type=="last_name":
            if sort_direction=="asc":
                return {key: value for key, value in sorted(bank_accounts.items(), key=lambda item: item[1].last_name)}
            else:
                return {key: value for key, value in sorted(bank_accounts.items(), key=lambda item: item[1].last_name,reverse=True)} 
        elif sort_type=="balance":
            if sort_direction=="asc":
                return {key: value for key, value in sorted(bank_accounts.items(), key=lambda item: item[1].balance)}
            else:
                return {key: value for key, value in sorted(bank_accounts.items(), key=lambda item: item[1].balance,reverse=True)} 

    def export_statement(self, bank_accounts, account_number, output_file):
        '''Exports the given account information to the given output file in the following format:

        First Name: Huize
        Last Name: Huang
        Balance: 34.57
        '''

        # TODO insert your code
        first_name=bank_accounts[account_number].first_name
        last_name=bank_accounts[account_number].last_name
        balance=bank_accounts[account_number].balance
        with open(output_file,"w") as f:
            f.write("/n")
            f.write(f"First Name: {first_name}"+"/n")
            f.write(f"Last Name: {last_name}"+"/n")
            f.write(f"Balance: {balance}"+"/n")