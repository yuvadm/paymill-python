__author__ = 'yalnazov'
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from paymill.paymill_context import PaymillContext
from paymill.models.subscription import Subscription
import test_config


class TestTransactionService(unittest.TestCase):

    amount = 4200
    currency = 'EUR'
    description = 'Test Python'

    def setUp(self):
        self.p = PaymillContext(api_key=test_config.api_key)
        self.transaction = self.p.get_transaction_service().create_with_token(token=test_config.magic_token,
                                                                              amount=TestTransactionService.amount,
                                                                              currency=TestTransactionService.currency,
                                                                              description=TestTransactionService.description)

    def test_create_sets_amount(self):
        self.assertEqual(TestTransactionService.amount, self.transaction.amount)

    def test_create_sets_currency(self):
        self.assertEqual(TestTransactionService.currency, self.transaction.currency)

    def test_create_sets_description(self):
        self.assertEqual(TestTransactionService.description, self.transaction.description)