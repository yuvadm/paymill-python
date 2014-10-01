# coding=utf-8
__author__ = 'yalnazov'

from . import utils.http_client
from . import services.client_service
from . import services.offer_service
from . import services.payment_service
from . import services.preauthorization_service
from . import services.refund_service
from . import services.subscription_service
from . import services.transaction_service
from . import services.webhook_service


class PaymillContext(object):

    """Entry point for PAYMILL API.
       Use the getter methods in order to access the required PAYMILL service.
    """

    def __init__(self, api_key):
        """
        :param str api_key: your PAYMILL private key
        :rtype : PaymillContext
        """
        self.api_url = 'https://api.paymill.com/v2.1'
        self.api_key = api_key
        self.http_client = utils.http_client.HTTPClient(self.api_url, api_key, "")
        self.client_service = services.client_service.ClientService(self.http_client)
        self.offer_service = services.offer_service.OfferService(self.http_client)
        self.payment_service = services.payment_service.PaymentService(self.http_client)
        self.preauthorization_service = services.preauthorization_service.PreauthorizationService(self.http_client)
        self.refund_service = services.refund_service.RefundService(self.http_client)
        self.subscription_service = services.subscription_service.SubscriptionService(self.http_client)
        self.transaction_service = services.transaction_service.TransactionService(self.http_client)
        self.webhook_service = services.webhook_service.WebhookService(self.http_client)

    """Getter methods for each PAYMILL service."""

    def get_client_service(self):
        return self.client_service

    def get_offer_service(self):
        return self.offer_service

    def get_payment_service(self):
        return self.payment_service

    def get_preauthorization_service(self):
        return self.preauthorization_service

    def get_refund_service(self):
        return self.refund_service

    def get_subscription_service(self):
        return self.subscription_service

    def get_transaction_service(self):
        return self.transaction_service

    def get_webhook_service(self):
        return self.webhook_service