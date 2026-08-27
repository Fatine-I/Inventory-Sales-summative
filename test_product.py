import unittest
from product_class import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product=Product("P001","rice",50.0,20)

    def test_product(self):
        self.assertEqual(self.product.name,"rice")
        self.assertEqual(self.product.price,50.0)
        self.assertEqual(self.product.quantity,20)

    def test_price(self):
        self.product.price=-50.0
        self.assertEqual(self.product.price,50.0)

    def test_add_product(self):
        result=self.product.add_quantity(10)
        self.assertTrue(result)
        self.assertEqual(self.product.quantity,30)

    def test_reduce_quantity(self):
        result=self.product.reduce_quantity(5)
        self.assertTrue(result)
        self.assertEqual(self.product.quantity,15)

    def test_prevent_insufficient_stock(self):
        result=self.product.reduce_quantity(30)
        self.assertFalse(result)
        self.assertEqual(self.product.quantity,20)

    def test_low_stock(self):
        self.product.reduce_quantity(16)
        self.assertTrue(self.product.is_low_stock)

    if __name__=="__main__":
        unittest.main()
