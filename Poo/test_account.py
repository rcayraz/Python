import unittest
from account import Account

class TestAccount(unittest.TestCase):
    def test_initial_amount(self):
        account = Account(1000)
        self.assertEqual(account.amount, 1000)

    def test_set_positive_amount(self):
        account = Account(1000)
        account.amount = 500
        self.assertEqual(account.amount, 500)

    def test_set_negative_amount(self):
        account = Account(1000)
        account.amount = -1000
        self.assertEqual(account.amount, 0)

if __name__ == '__main__':
    unittest.main()