from ProductBase_class import ProductBase

class Product(ProductBase):

    def __init__(self, product_id, name, price, quantity, low_stock_level=5):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__low_stock_level = low_stock_level

    # Getter methods
    @property
    def product_id(self):
        return self.__product_id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    @property
    def low_stock_level(self):
        return self.__low_stock_level

    # Setter methods
    @name.setter
    def name(self, new_name):
        if new_name.strip() == "":
            return False

        self.__name = new_name
        return True
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            return False

        self.__price = new_price
        return True

    @low_stock_level.setter
    def low_stock_level(self, new_level):
        if new_level < 0:
            return False

        self.__low_stock_level = new_level
        return True

