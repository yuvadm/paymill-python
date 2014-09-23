__author__ = 'yalnazov'
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from paymill.paymill_context import PaymillContext
import test_config


class TestPreauthorizationService(unittest.TestCase):

    amount = '4200'
    currency = 'EUR'
    description = 'Test Python'

    def setUp(self):
        self.p = PaymillContext(api_key=test_config.api_key)
        self.preauthorization = self.p.get_preauthorization_service().create_with_token(token=test_config.magic_token,
                                                                                        amount=TestPreauthorizationService.amount,
                                                                                        currency=TestPreauthorizationService.currency,
                                                                                        description=TestPreauthorizationService.description)

    def test_create_sets_amount(self):
        self.assertEqual(TestPreauthorizationService.amount, self.preauthorization.amount)

    def test_create_sets_currency(self):
        self.assertEqual(TestPreauthorizationService.currency, self.preauthorization.currency)

    def test_create_sets_description(self):
        self.assertEqual(TestPreauthorizationService.description, self.preauthorization.description)
