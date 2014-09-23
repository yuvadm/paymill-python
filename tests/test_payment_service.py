__author__ = 'yalnazov'
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from paymill.paymill_context import PaymillContext
from paymill.models.payment import Payment
import test_config


class TestPaymentService(unittest.TestCase):

    def setUp(self):
        self.p = PaymillContext(test_config.api_key)
        self.payment = None

    def tearDown(self):
        del self.p

    def test_create_payment_with_token_default(self):
        p1 = self.p.get_payment_service().create(token=test_config.magic_token)
        self.assertEqual(None, p1.client)

    def test_create_payment_with_client(self):
        p1 = self.p.get_payment_service().create(token=test_config.magic_token,
                                                 client_id='client_33baaf3ee3251b083420')

        self.assertEqual('client_33baaf3ee3251b083420', p1.client.id)

    def test_delete_payment(self):
        p1 = self.p.get_payment_service().create(token=test_config.magic_token)
        self.assertIsInstance(self.p.get_payment_service().remove(p1), Payment)