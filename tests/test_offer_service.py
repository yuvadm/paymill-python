__author__ = 'yalnazov'
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from paymill.paymill_context import PaymillContext
from paymill.models.offer import Offer
import test_config


class TestOfferService(unittest.TestCase):

    def setUp(self):
        self.p = PaymillContext(test_config.api_key)
        self.offer = None

    def tearDown(self):
        del self.p

    def test_create_offer_default(self):
        o = self.p.get_offer_service().create(100, 'EUR', '1 MONTH', 'My offer')
        self.assertEqual('My offer', o.name)

    def test_create_offer_with_trial_period(self):
        o = self.p.get_offer_service().create(100, 'EUR', '1 MONTH', 'My offer', 2)
        self.assertEqual(2, o.trial_period_days)

    def test_delete_offer(self):
        o = self.p.get_offer_service().create(100, 'EUR', '1 MONTH', 'My offer')
        self.assertIsInstance(self.p.get_offer_service().remove(o), Offer)