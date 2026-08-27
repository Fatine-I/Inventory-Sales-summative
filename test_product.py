import unittest
from product_class import Product

class testproduct(unittest.TestCase):
    def setUp(self):
        self.product=Product("P001","rice",50.0,20)

    def test_create_product(self):
        self.assertEqual(self.product.name(),"rice")
        self.assertEqual(self.product.price(),50.0)
        self.assertEqual(self.product.quantity(),20)

    def test_set_vaid_price(self):
        result=self.product.price(-50.0)
        self.assertFalse(result)
        self.assertEqual(self.product.price(),50.0)
        