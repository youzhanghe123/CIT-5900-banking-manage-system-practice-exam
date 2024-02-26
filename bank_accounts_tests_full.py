import unittest

from AccountCreator import *
from AccountManager import *

class Accounts_Tests(unittest.TestCase):

    def setUp(self):
        #create instance of AccountCreator
        account_creator = AccountCreator()
        #attach test data to self
        self.bank_accounts = account_creator.init_bank_accounts('accounts.txt', 'deposits.csv', 'withdrawals.csv')
        #create instance of AccountManager
        self.account_manager = AccountManager()
        self.bank_accounts_to_sort = {
            '1': Account('1', 'Abbey', 'Krane'),
            '2': Account('2', 'Bob', 'Williams'),
            '3': Account('3', 'Corey', 'Smith')
        }
        
        self.bank_accounts_to_sort['1'].balance = 5000
        self.bank_accounts_to_sort['2'].balance = 500
        self.bank_accounts_to_sort['3'].balance = 50
        

    def test_init_bank_accounts(self):

        # get balance of existing accounts

        #6685.99 - 128.4 = 6557.59
        self.assertAlmostEqual(6557.59, self.bank_accounts['1'].balance)

        #4739.87 - 22.98
        self.assertAlmostEqual(4716.89, self.bank_accounts['2'].balance)

        #0 - 0
        self.assertEqual(0.0, self.bank_accounts['7'].balance)

        #0 - 0
        self.assertEqual(0.0, self.bank_accounts['10'].balance)


    def test_get_account(self):

        #get account info from existing accounts
        account_info = self.account_manager.get_account(self.bank_accounts, '1')
        self.assertAlmostEqual(6557.59, account_info.balance)
        self.assertEqual('Brandon', account_info.first_name)
        self.assertEqual('Krakowsky', account_info.last_name)

        account_info = self.account_manager.get_account(self.bank_accounts, '2')
        self.assertAlmostEqual(4716.89, account_info.balance)

        account_info = self.account_manager.get_account(self.bank_accounts, '7')
        self.assertEqual(0.0, account_info.balance)
        self.assertEqual('Huize', account_info.first_name)
        self.assertEqual('Huang', account_info.last_name)

        account_info = self.account_manager.get_account(self.bank_accounts, '10')
        self.assertEqual(0.0, account_info.balance)

        #get account info from non-existant account
        account_info = self.account_manager.get_account(self.bank_accounts, '1234')
        self.assertEqual(None, account_info)

    def test_withdraw(self):

        #withdraw from existing accounts
        self.assertAlmostEqual(6700.19, self.account_manager.get_account(self.bank_accounts, '6').balance)
        self.account_manager.withdraw(self.bank_accounts, '6', .19)
        #6700.19 - .19 = 6700.00
        self.assertAlmostEqual(6700.00, self.account_manager.get_account(self.bank_accounts, '6').balance)

        self.assertAlmostEqual(651.44, self.account_manager.get_account(self.bank_accounts, '9').balance)
        self.account_manager.withdraw(self.bank_accounts, '9', 651)
        #651.44 - 651 = .44
        self.assertAlmostEqual(.44, self.account_manager.get_account(self.bank_accounts, '9').balance)

        # withdraw too much
        self.assertEqual(0.0, self.account_manager.get_account(self.bank_accounts, '10').balance)
        #0.0 - .1 = RuntimeError
        self.assertRaises(RuntimeError, self.account_manager.withdraw, self.bank_accounts, '10', .1)

        #withdraw from non-existant accounts
        self.account_manager.withdraw(self.bank_accounts, '3ew231', 1.99)

    def test_deposit(self):

        # deposit to existing accounts
        self.assertAlmostEqual(6700.19, self.account_manager.get_account(self.bank_accounts, '6').balance)
        self.account_manager.deposit(self.bank_accounts, '6', 1)
        #6700.19 + 1 = 6701.19
        self.assertAlmostEqual(6701.19, self.account_manager.get_account(self.bank_accounts, '6').balance)

        self.assertAlmostEqual(651.44, self.account_manager.get_account(self.bank_accounts, '9').balance)
        self.account_manager.deposit(self.bank_accounts, '9', 1000.01)
        # 651.44 + 1000.01 = 1651.45
        self.assertAlmostEqual(1651.45, self.account_manager.get_account(self.bank_accounts, '9').balance)

        self.assertEqual(0.0, self.account_manager.get_account(self.bank_accounts, '10').balance)
        self.account_manager.deposit(self.bank_accounts, '10', 0)
        # 0.0 + 0 = 0.0
        self.assertEqual(0.0, self.account_manager.get_account(self.bank_accounts, '10').balance)

        # deposit to non-existent account
        self.account_manager.deposit(self.bank_accounts, '3ew231', 1.99)

    def test_purchase(self):

        # purchase from existing accounts
        self.assertAlmostEqual(4716.89, self.account_manager.get_account(self.bank_accounts, '2').balance)
        self.account_manager.purchase(self.bank_accounts, '2', [3.2, 4.89, 32.9])
        #4716.89 - (40.99 + 2.46) = 4673.44
        self.assertAlmostEqual(4673.44, self.account_manager.get_account(self.bank_accounts, '2').balance, 2)

        self.assertAlmostEqual(6557.59, self.account_manager.get_account(self.bank_accounts, '1').balance)
        # 6557.59 - (6557.59 + 393.46) = RuntimeError
        self.assertRaises(RuntimeError, self.account_manager.purchase, self.bank_accounts, '1', [6557, .59])

        self.assertAlmostEqual(651.44, self.account_manager.get_account(self.bank_accounts, '9').balance)
        # 651.44 - (651.45 + 39.087) = RuntimeError
        self.assertRaises(RuntimeError, self.account_manager.purchase, self.bank_accounts, '9', [.45, 651])

        # purchase from non-existent account
        self.account_manager.purchase(self.bank_accounts, '3425', [1.99])

    def test_sort_accounts(self):
        #sort by account_number ascending
        sorted_accounts = self.account_manager.sort_accounts(self.bank_accounts_to_sort, 'account_number', 'asc')
        sorted_keys = [account[0] for account in sorted_accounts]
        expected_order = ['1', '2', '3']
        self.assertEqual(sorted_keys, expected_order)
        
        #sort by account_number descending
        sorted_accounts = self.account_manager.sort_accounts(self.bank_accounts_to_sort, 'account_number', 'desc')
        sorted_keys = [account[0] for account in sorted_accounts]
        expected_order = ['3', '2', '1']
        self.assertEqual(sorted_keys, expected_order)
        
        #sort by first_name ascending
        sorted_accounts = self.account_manager.sort_accounts(self.bank_accounts_to_sort, 'first_name', 'asc')
        sorted_keys = [account[0] for account in sorted_accounts]
        expected_order = ['1', '2', '3'] # Abbey < Bob < Corey
        self.assertEqual(sorted_keys, expected_order)
        
        #sort by first_name descending
        sorted_accounts = self.account_manager.sort_accounts(self.bank_accounts_to_sort, 'first_name', 'desc')
        sorted_keys = [account[0] for account in sorted_accounts]
        expected_order = ['3', '2', '1']
        self.assertEqual(sorted_keys, expected_order) # Corey > Bob > Abbey
        
        #sort by last_name ascending
        sorted_accounts = self.account_manager.sort_accounts(self.bank_accounts_to_sort, 'last_name', 'asc')
        sorted_keys = [account[0] for account in sorted_accounts]
        expected_order = ['1', '3', '2']
        self.assertEqual(sorted_keys, expected_order) # Krane < Smith < Williams
        
        #sort by last_name descending
        sorted_accounts = self.account_manager.sort_accounts(self.bank_accounts_to_sort, 'last_name', 'desc')
        sorted_keys = [account[0] for account in sorted_accounts]
        expected_order = ['2', '3', '1']
        self.assertEqual(sorted_keys, expected_order) # Williams > Smith > Krane
        
        #sort by balance ascending
        sorted_accounts = self.account_manager.sort_accounts(self.bank_accounts_to_sort, 'balance', 'asc')
        sorted_keys = [account[0] for account in sorted_accounts]
        expected_order = ['3', '2', '1']
        self.assertEqual(sorted_keys, expected_order) # 50 < 500 < 5000
        
        
        #sort by balance descending
        sorted_accounts = self.account_manager.sort_accounts(self.bank_accounts_to_sort, 'balance', 'desc')
        sorted_keys = [account[0] for account in sorted_accounts]
        expected_order = ['1', '2', '3']
        self.assertEqual(sorted_keys, expected_order) # 5000 > 500 > 50

    def test_export_statement(self):
        # check file exports for correct formatting of the info
        self.account_manager.export_statement(self.bank_accounts, '3', '3.txt')
        self.account_manager.export_statement(self.bank_accounts, '4', '4.txt')
        self.account_manager.export_statement(self.bank_accounts, '5', '5.txt')


if __name__ == '__main__':
    unittest.main()