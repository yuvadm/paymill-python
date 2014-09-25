__author__ = 'yalnazov'

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from paymill.paymill_context import PaymillContext
import paymill.models
from paymill.models.paymill_list import PaymillList
import datetime
import calendar
import test_config


class TestClientService(unittest.TestCase):

    def setUp(self):
        self.p = PaymillContext(test_config.api_key)
        self.client = None

    def tearDown(self):
        del self.p

    def test_create_client_with_email(self):
        c = self.p.client_service.create(email="test@mail.com")
        self.assertIsInstance(c.payment, list)
        self.assertEqual(0, len(c.payment))
        self.assertEqual("test@mail.com", c.email)

    def test_create_client_with_description(self):
        c = self.p.client_service.create(description="voucher")
        self.assertEqual("voucher", c.description)

    def test_update_client_with_email(self):
        c = self.p.client_service.create(email="test@mail.com")
        c.email = "test2@mail.com"
        self.assertEqual("test2@mail.com", self.p.client_service.update(c).email)

    def test_update_client_with_description(self):
        c = self.p.client_service.create(description="voucher")
        c.description = "voucher2"
        self.assertEqual("voucher2", self.p.client_service.update(c).description)

    def test_remove_client(self):
        c = self.p.client_service.create(email="delete@mail.com")
        self.assertIsInstance(self.p.client_service.remove(c), paymill.models.client.Client)

    def test_detail_client(self):
        c = self.p.client_service.create(email="details@mail.com")
        self.assertEqual("details@mail.com", self.p.client_service.detail(c).email)
    
    def test_list_clients_default(self):
        #add at least one to the list
        self.p.client_service.create(email="test@mail.com")
        self.assertIsInstance(self.p.client_service.list(), PaymillList)

    def test_list_clients_with_filter(self):
        c = self.p.client_service.create(email="new_client@mail.com")
        past = calendar.timegm((datetime.datetime.utcnow() - datetime.timedelta(minutes=5)).timetuple())
        clients = self.p.client_service.list(filtr=paymill.models.client.Client.Filter.by_created_at(past))
        for cl in clients.data:
            self.assertNotEquals(c.id, cl.id)

    def test_list_clients_with_order(self):
        cl = self.p.client_service.list()
        lo = self.p.client_service.list(order=paymill.models.client.Client.Order.email().asc())
        self.assertNotEquals(cl.data[0], lo.data[0])