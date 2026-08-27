class Sale:

    def __init__(self,sale_id,product_id,product_name,quantity_sold,unit_price):
        self.__sale_id = sale_id
        self.__product_id = product_id
        self.__product_name = product_name
        self.__quantity_sold = quantity_sold
        self.__unit_price = unit_price
        self.__total_cost = quantity_sold * unit_price

    
    @property
    def sale_id(self):
        return self.__sale_id

    @property
    def product_id(self):
        return self.__product_id

    @property
    def product_name(self):
        return self.__product_name

    @property
    def quantity_sold(self):
        return self.__quantity_sold

    @property
    def unit_price(self):
        return self.__unit_price

    @property
    def total_cost(self):
        return self.__total_cost

    # Display sale details

    def display_details(self):
        print("\n------ SALE DETAILS ------")
        print(f"Sale ID: {self.__sale_id}")
        print(f"Product ID: {self.__product_id}")
        print(f"Product Name: {self.__product_name}")
        print(f"Quantity Sold: {self.__quantity_sold}")
        print(f"Unit Price: {self.__unit_price:.2f}")
        print(f"Total Cost: {self.__total_cost:.2f}")
        print("--------------------------")

    # Convert Sale object into dictionary

    def to_dictionary(self):
        return {
            "sale_id": self.__sale_id,
            "product_id": self.__product_id,
            "product_name": self.__product_name,
            "quantity_sold": self.__quantity_sold,
            "unit_price": self.__unit_price
        }