__author__ = 'yalnazov'
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from paymill.paymill_context import PaymillContext
from paymill.models.subscription import Subscription
import test_config


class TestSubscriptionService(unittest.TestCase):

    currency = 'EUR'
    interval = '2 DAY'
    amount = 4200
    sub_dict = {u'livemode': False,
                u'updated_at': 1409647372,
                u'currency': u'EUR',
                u'id': u'sub_edacd9959b10c8f6eb5d',
                u'is_canceled': False,
                u'next_capture_at': 1409820171,
                u'temp_amount': None,
                u'status': u'active',
                u'trial_start': None,
                u'offer': {u'subscription_count': {u'active': u'1', u'inactive': 0},
                           u'name': u'', u'created_at': 1409647371,
                           u'interval': u'2 DAY',
                           u'updated_at': 1409647371,
                           u'app_id': None,
                           u'currency': u'EUR',
                           u'amount': u'4200',
                           u'trial_period_days': None,
                           u'id': u'offer_bb33ea77b942f570997b'},
                u'app_id': None,
                u'trial_end': None,
                u'payment': {u'app_id': None,
                             u'is_recurring': True,
                             u'expire_month': u'12',
                             u'country': None,
                             u'created_at': 1409647371,
                             u'updated_at': 1409647371,
                             u'card_holder': u'',
                             u'card_type': u'visa',
                             u'last4': u'1111',
                             u'is_usable_for_preauthorization': True,
                             u'client': u'client_4b6fc054e35ba1548959',
                             u'expire_year': u'2015',
                             u'type': u'creditcard',
                             u'id': u'pay_3dca8cabea90e752ed7be662'},
                u'is_deleted': False,
                u'name': u'',
                u'end_of_period': None,
                u'canceled_at': None,
                u'created_at': 1409647371,
                u'interval': u'2 DAY',
                u'amount': 4200,
                u'client': {u'description': None,
                            u'payment': [u'pay_3dca8cabea90e752ed7be662'],
                            u'created_at': 1409647371,
                            u'updated_at': 1409647371,
                            u'app_id': None,
                            u'email': None,
                            u'id': u'client_4b6fc054e35ba1548959',
                            u'subscription': None},
                u'period_of_validity': None}

    def setUp(self):
        self.p = PaymillContext(test_config.api_key)
        self.payment = self.p.get_payment_service().create(test_config.magic_token)
        self.subscription = self.p.get_subscription_service().create_with_amount(self.payment.id,
                                                                                 TestSubscriptionService.amount,
                                                                                 TestSubscriptionService.currency,
                                                                                 TestSubscriptionService.interval)

    def tearDown(self):
        del self.p, self.payment, self.subscription

    def test_serialize_subscription_to_dict(self):
        self.assertIsInstance(TestSubscriptionService.sub_dict, dict)

    def test_serialize_subscription_to_Subscription(self):
        s = Subscription(TestSubscriptionService.sub_dict)
        self.assertIsInstance(s, Subscription)
        self.assertEqual(1409647372, s.updated_at)

    def test_create_subscription_sets_client_id(self):
        self.assertIsNotNone(self.subscription.client.id)

    def test_subscription_create_sets_payment_id(self):
        self.assertEqual(self.payment.id, self.subscription.payment.id)

    def test_subscription_create_sets_amount(self):
        self.assertEqual(TestSubscriptionService.amount, self.subscription.amount)

    def test_subscription_create_sets_currency(self):
        self.assertEqual(TestSubscriptionService.currency, self.subscription.currency)

    def test_subscription_create_sets_interval(self):
        self.assertEqual(TestSubscriptionService.interval, self.subscription.interval)

    def test_subscription_update_default_sets_interval(self):
        p = PaymillContext(test_config.api_key)
        payment = p.get_payment_service().create(test_config.magic_token)
        subscription = p.get_subscription_service().create_with_amount(payment.id,
                                                                       TestSubscriptionService.amount,
                                                                       TestSubscriptionService.currency,
                                                                       TestSubscriptionService.interval)
        subscription.interval = '1 MONTH,FRIDAY'
        s = p.get_subscription_service().update(subscription)
        self.assertEqual('1 MONTH,FRIDAY', s.interval)

    def test_subscription_update_with_amount_sets_amount(self):
        p = PaymillContext(test_config.api_key)
        payment = p.get_payment_service().create(test_config.magic_token)
        subscription = p.get_subscription_service().create_with_amount(payment.id,
                                                                       TestSubscriptionService.amount,
                                                                       TestSubscriptionService.currency,
                                                                       TestSubscriptionService.interval)
        subscription.amount = 5600
        s = p.get_subscription_service().update_with_amount(subscription, amount_change_type=1)
        self.assertEqual(5600, s.amount)

    def test_subscription_cancel(self):
        p = PaymillContext(test_config.api_key)
        payment = p.get_payment_service().create(test_config.magic_token)
        subscription = p.get_subscription_service().create_with_amount(payment.id,
                                                                       TestSubscriptionService.amount,
                                                                       TestSubscriptionService.currency,
                                                                       TestSubscriptionService.interval)
        s = p.get_subscription_service().cancel(subscription)
        self.assertIsInstance(s, Subscription)
