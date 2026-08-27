import unittest

from sales_class import Sale


class TestSale(unittest.TestCase):

    def setUp(self):
        self.sale = Sale(
            "S001",
            "P001",
            "Rice",
            5,
            50.0
        )

    def test_create_sale(self):
        self.assertEqual(
            self.sale.sale_id,
            "S001"
        )

        self.assertEqual(
            self.sale.product_id,
            "P001"
        )

    def test_product_name(self):
        self.assertEqual(
            self.sale.product_name,
            "Rice"
        )

    def test_quantity_sold(self):
        self.assertEqual(
            self.sale.quantity_sold,
            5
        )

    def test_unit_price(self):
        self.assertEqual(
            self.sale.unit_price,
            50.0
        )

    def test_total_cost(self):
        self.assertEqual(
            self.sale.total_cost,
            250.0
        )

    def test_to_dictionary(self):
        data = self.sale.to_dictionary()

        self.assertEqual(
            data["sale_id"],
            "S001"
        )

        self.assertEqual(
            data["quantity_sold"],
            5
        )

        self.assertEqual(
            data["unit_price"],
            50.0
        )


if __name__ == "__main__":
    unittest.main()