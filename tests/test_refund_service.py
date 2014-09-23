__author__ = 'yalnazov'
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from paymill.paymill_context import PaymillContext
from paymill.models.subscription import Subscription
import test_config


class TestRefundService(unittest.TestCase):

    amount = 4200
    currency = 'EUR'
    description = 'Test Python'

    def setUp(self):
        self.p = PaymillContext(api_key=test_config.api_key)

    def test_refund(self):
        transaction = self.p.get_transaction_service().create_with_token(token=test_config.magic_token,
                                                                         amount=TestRefundService.amount,
                                                                         currency=TestRefundService.currency,
                                                                         description=TestRefundService.description)


        refund = self.p.get_refund_service().refund_transaction(transaction_id=transaction.id,
                                                                amount=TestRefundService.amount)

        self.assertEqual(TestRefundService.amount, refund.amount)