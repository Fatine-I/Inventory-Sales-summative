import json

from product_class import Product
from sales_class import Sale


class Inventory:

    def __init__(self):
        self.products = []
        self.sales = []

    # Product methods

    def add_product(self, product):
        if self.search_product(product.product_id) is not None:
            return False
        self.products.append(product)
        return True

    def display_all_products(self):
        if len(self.products) == 0:
            print("\nNo products available.")
            return
        for product in self.products:
            product.display_details()

    def search_product(self, product_id):
        for product in self.products:
            # Fixed: product_id is a property, not a method call
            if product.product_id.lower() == product_id.lower():
                return product
        return None

    def update_product_information(self, product_id, new_name, new_price):
        product = self.search_product(product_id)
        
        if product is None:
            return False

        # Fixed: use property assignment instead of non-existent set_ methods
        try:
            product.name = new_name
            product.price = new_price
            return True
        except ValueError:
            return False

    def update_product_quantity(self, product_id, amount):
        product = self.search_product(product_id)
        if product is None:
            return False
        return product.add_quantity(amount)

    # Sale methods

    def generate_sale_id(self):
        return f"S{len(self.sales) + 1:03d}"

    def record_sale(self, product_id, quantity_sold):
        product = self.search_product(product_id)

        if product is None:
            return None, "Product not found."

        if quantity_sold <= 0:
            return None, "Sale quantity must be greater than zero."

        if quantity_sold > product.quantity:
            return None, "Insufficient stock."

        sale_id = self.generate_sale_id()
        sale = Sale(
            sale_id,
            product.product_id,
            product.name,
            quantity_sold,
            product.price,
        )

        product.reduce_quantity(quantity_sold)
        self.sales.append(sale)

        return sale, "Sale completed successfully."

    def display_all_sales(self):
        if len(self.sales) == 0:
            print("\nNo sales available.")
            return
        for sale in self.sales:
            sale.display_details()

    def display_low_stock_products(self):
        low_stock_products = []

        for product in self.products:
            # Fixed: added parentheses because is_low_stock is a method
            if product.is_low_stock():
                low_stock_products.append(product)

        if len(low_stock_products) == 0:
            print("\nThere are no low stock products.")
            return

        print("\n-----+ LOW STOCK PRODUCTS -----")
        for product in low_stock_products:
            product.display_details()

    # Save product data
    def save_products(self, filename):
        data = []
        for product in self.products:
            data.append(product.to_dictionary())
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    # Load product data
    def load_products(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for item in data:
                    product = Product(
                        item["product_id"],
                        item["name"],
                        item["price"],
                        item["quantity"],
                        item.get("low_stock_level", 5),
                    )
                    self.products.append(product)
        except FileNotFoundError:
            print(
                "Product data file not found. Starting with an empty inventory."
            )
        except json.JSONDecodeError:
            print("Product data file contains invalid data.")

    # Save sales data
    def save_sales(self, filename):
        data = []
        for sale in self.sales:
            data.append(sale.to_dictionary())
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    # Load sales data
    def load_sales(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for item in data:
                    sale = Sale(
                        item["sale_id"],
                        item["product_id"],
                        item["product_name"],
                        item["quantity_sold"],
                        item["unit_price"],
                    )
                    self.sales.append(sale)
        except FileNotFoundError:
            print("Sales data file not found. Starting with no sales.")
        except json.JSONDecodeError:
            print("Sales data file contains invalid data.")