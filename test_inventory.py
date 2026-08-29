import unittest

from inventory_class import Inventory
from product_class import Product


class TestInventory(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()

        self.product = Product("P001", "Rice", 50.0, 20)

    def test_add_product(self):
        result = self.inventory.add_product(self.product)

        self.assertTrue(result)

        self.assertEqual(len(self.inventory.products), 1)

    def test_prevent_duplicate_product_id(self):
        self.inventory.add_product(self.product)

        duplicate_product = Product("P001", "Rice Premium", 75.0, 10)

        result = self.inventory.add_product(duplicate_product)

        self.assertFalse(result)

        self.assertEqual(len(self.inventory.products), 1)

    def test_search_existing_product(self):
        self.inventory.add_product(self.product)

        result = self.inventory.search_product("P001")

        self.assertIsNotNone(result)

        # Fixed: access via property instead of get_name() method
        self.assertEqual(result.name, "Rice")

    def test_search_non_existing_product(self):
        result = self.inventory.search_product("P999")

        self.assertIsNone(result)

    def test_update_product_information(self):
        self.inventory.add_product(self.product)

        result = self.inventory.update_product_information(
            "P001", "Premium Rice", 70.0
        )

        self.assertTrue(result)

        product = self.inventory.search_product("P001")

        # Fixed: access via property instead of method calls
        self.assertEqual(product.name, "Premium Rice")

        self.assertEqual(product.price, 70.0)

    def test_update_product_quantity(self):
        self.inventory.add_product(self.product)

        result = self.inventory.update_product_quantity("P001", 10)

        self.assertTrue(result)

        product = self.inventory.search_product("P001")

        # Fixed: access via property instead of get_quantity()
        self.assertEqual(product.quantity, 30)

    def test_record_valid_sale(self):
        self.inventory.add_product(self.product)

        sale, message = self.inventory.record_sale("P001", 5)

        self.assertIsNotNone(sale)

        # Fixed: access via property instead of get_total_cost()
        self.assertEqual(sale.total_cost, 250.0)

        self.assertEqual(self.product.quantity, 15)

    def test_prevent_insufficient_stock_sale(self):
        self.inventory.add_product(self.product)

        sale, message = self.inventory.record_sale("P001", 30)

        self.assertIsNone(sale)

        self.assertEqual(message, "Insufficient stock.")

        self.assertEqual(self.product.quantity, 20)


if __name__ == "__main__":
    unittest.main()