__author__ = 'yalnazov'

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from paymill.utils.http_client import HTTPClient


class TestHTTPClient(unittest.TestCase):
    """

    Testing all local methods of the HTTPClient abstraction

    """

    api_key = '20a690e5283cd3419629a42cc8631193'
    api_url = 'https://api.paymill.com/v2.1'

    def setUp(self):
        self.http_client = HTTPClient(TestHTTPClient.api_url, TestHTTPClient.api_key)

    def test_client_init(self):
        c = HTTPClient(self.api_url, self.api_key)
        self.assertIsInstance(c, HTTPClient)

    def test_client_init_sets_url(self):
        self.assertEqual(
            self.http_client.base_url, TestHTTPClient.api_url)

    def test_client_init_sets_user_and_pass(self):
        self.assertEqual(self.http_client.session.auth, (TestHTTPClient.api_key, ''))

    # def test_client_deserliaze_pm_list(self):
    #     items, count = self.http_client._deserialize(json.loads('{"data":[], '
    #                                                             '"data_count":"0", '
    #                                                             '"mode":"test"}'), return_type=Client)
    #
    #     self.assertListEqual(PaymillList().items, PaymillList(items=items, count=count).items)
    #
    # def test_client_deserliaze_client_pm_list(self):
    #     items, count = self.http_client._deserialize(json.loads('{"data":[{'
    #                                                             '"id": "client_bc798246e32ce7e66dbe",'
    #                                                             '"email": null, '
    #                                                             '"description": null, '
    #                                                             '"created_at": 1342427064, '
    #                                                             '"updated_at": 1342427064, '
    #                                                             '"payment": null, '
    #                                                             '"subscription": null,  '
    #                                                             '"app_id": null }], '
    #                                                             '"data_count":"1", '
    #                                                             '"mode":"test"}'), return_type=Client)
    #
    #     expected = Client(**dict(id='client_bc798246e32ce7e66dbe', email=None, description=None,
    #                            created_at=1342427064, updated_at=1342427064, payment=None,
    #                            subscription=None, app_id=None))
    #
    #     self.assertEqual(PaymillList(items=[expected]).items[0].id,
    #                      PaymillList(items=items, count=count).items[0].id)




