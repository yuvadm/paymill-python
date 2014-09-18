__author__ = 'yalnazov'
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from paymill import PaymillContext
from paymill.models.webhook import Webhook
import test_config


class TestWebhookService(unittest.TestCase):

    amount = 4200
    currency = 'EUR'
    description = 'Test Python'

    def setUp(self):
        self.p = PaymillContext(api_key=test_config.api_key)

    def test_webhook(self):
        webhook = self.p.get_webhook_service().create_email('yalnazov@gmail.com', ['subscription.succeeded'], True)

        self.assertIsInstance(webhook, Webhook)