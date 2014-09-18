__author__ = 'yalnazov'

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from paymill.models.order import Order


class TestOrder(unittest.TestCase):
    """

    Testing all methods of the Order abstraction

    """

    def setUp(self):
        self.order = Order('email')

    def test_order_init(self):
        o = Order('test')
        self.assertIsInstance(o, Order)

    def test_order_init_sets_typ(self):
        o = Order('test')
        self.assertEqual('test', o.typ)

    def test_order_asc(self):
        self.order.asc()
        self.assertEqual(True, self.order.ascending)

    def test_order_desc(self):
        self.order.desc()
        self.assertEqual(False, self.order.ascending)

    def test_order_to_dict(self):
        expected = dict(order='email_asc')
        self.order.ascending = True
        self.assertDictEqual(expected, self.order.to_dict())