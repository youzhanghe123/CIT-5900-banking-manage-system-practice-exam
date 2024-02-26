import os

from AccountCreator import *
from AccountManager import *

def main():
    # create instance of AccountCreator class
    account_creator = AccountCreator()

    # load and get all account info
    bank_accounts = account_creator.init_bank_accounts('accounts.txt', 'deposits.csv', 'withdrawals.csv')

    # create instance of AccountManager class
    account_manager = AccountManager()

    #for testing
    #print(bank_accounts)

    while True:

        #print welcome and options
        print('\nWelcome to the bank!  What would you like to do?')
        print('1: Get account info')
        print('2: Make a deposit')
        print('3: Make a withdrawal')
        print('4: Make a purchase')
        print('5: Sort accounts')
        print('6: Export a statement')
        print('0: Leave the bank')

        # get user input
        option_input = input('\n')

        # try to cast to int
        try:
            option = int(option_input)

        # catch ValueError
        except ValueError:
            print("Invalid option.")

        else:

            #check options
            if (option == 1):

                #get account number and print account info
                account_number = input('Account number? ')
                print(account_manager.get_account(bank_accounts, account_number))

            elif (option == 2):

                # get account number and amount and make deposit
                account_number = input('Account number? ')

                # input cast to float
                amount = float(input('Amount? '))

                account_manager.deposit(bank_accounts, account_number, amount)

            elif (option == 3):

                # get account number and amount and make withdrawal
                account_number = input('Account number? ')

                #input cast to float
                amount = float(input('Amount?  '))

                account_manager.withdraw(bank_accounts, account_number, amount)

            elif (option == 4):

                # get account number and amounts and make purchase
                account_number = input('Account number? ')
                amounts = input('Amounts (as comma separated list)? ')

                # convert given amounts to list
                amount_list = amounts.split(',')
                amount_list = [float(i) for i in amount_list]

                account_manager.purchase(bank_accounts, account_number, amount_list)

            elif (option == 5):

                # get sort type
                sort_type = input("Sort type ('account_number', 'first_name', 'last_name', or 'balance')? ")

                # get sort direction
                sort_direction = input("Sort type ('asc' or 'desc')? ")

                sorted_accounts = account_manager.sort_accounts(bank_accounts, sort_type, sort_direction)
                
                for account_number, account in sorted_accounts:
                    print(f"{account}")

            elif (option == 6):

                # get account number to export
                account_number = input('Account number? ')

                account_manager.export_statement(bank_accounts, account_number, account_number + '.txt')

            elif (option == 0):

                # print message and leave the bank
                print('Goodbye!')
                break
            
if __name__ == "__main__":
    main()