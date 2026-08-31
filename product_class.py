from decimal import Decimal, InvalidOperation
from datetime import datetime


class Product:
    DATE_FORMAT="%d/%m/%Y"
    def __init__(self, product_id, name, price, quantity, category="", brand="", size="", supplier="", entry_date=None, expiry_date=None):
        self.product_id=self._validate_id(product_id)
        self.name=self._validate_text(name, "Product name")
        self.category=category.strip() if category else ""
        self.brand=brand.strip() if brand else ""
        self.size=size.strip() if size else ""
        self.supplier=supplier.strip() if supplier else ""
        self.price=self._validate_price(price)
        self.quantity=self._validate_quantity(quantity)
        self.entry_date=(self._validate_date(entry_date) if entry_date else datetime.now().strftime(self.DATE_FORMAT))
        Self.expiry_date=self._validate_date(expiry_date) if expiry_date else None


    @staticmethod
    def _validate_id(product_id):
        if product_id is None or str(product_id).strip()=="":
            raise ValueError("Product ID cannot be empty.")
        return str(product_id).strip()

    @staticmethod
    def _validate_text(value, field_name):
        if value is None or str(value).strip()=="":
            raise ValueError(f"{value} cannot be empty.")
        return str(value).strip()

    @staticmethod
    def _validate_price(price):
        try:
            price=Decimal(str(price))
        except(InvalidOperation,ValueError,TypeError):
            raise ValueError("Price must be a valid number.")
        if price <=0:
            raise ValueError("Price must be greater than zero.")
        return price
    
    @staticmethod
    def _validate_quantity(quantity):
        try:
            quantity=int(quantity)
        except (ValueError, TypeError):
            raise ValueError("Quantity must be a whole number.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        return quantity
    


    @classmethod
    def _validate_date(cls, date_str):
        try:
            datetime.strptime(date_str, cls.DATE_FORMAT)
        except (ValueError, TypeError):
            return ValueError(f"Date must be in {cls.DATE_FORMAT} format.")
        return date_str


    def update_price(self, new_price):
        self.price=self._validate_price(new_price)

    def update_quantity(self, new_quantity):
        self.quantity=self._validate_quantity(new_quantity)


    def reduce_quantity(self, amount):
        amount=self._validate_quantity(amount)
        if amount <=0:
            raise ValueError("Amount cannot be zero or negative")
        if amount > self.quantity:
            raise ValueError(f"Insuficient stock.\n Only {self.quantity} unit(s) is available.")
        self.quantity-=amount


    def increase_quantity(self, amount):
        amount=self._validate_quantity(amount)
        if amount <=0:
            raise ValueError("Amount cannot be zero or negative.")
        return self.quantity += amount


    def update_details(self, name=None, category=None, brand=None, size=None, supplier=None):
        if name is not None: 
            self.name=self._validate_text(name, "Product name")
        if category is not None:
            self.category=category.strip()
        if brand is not None:
            self.brand=brand.strip()
        if size is not None:
            self.size=size.strip()
        if supplier is not None:
            self.supplier=supplier.strip()



    def to_dict(self):
        return{
            "product_id": self.product_id,
            "name":self.name,
            "category": self.category,
            "brand": self.brand,
            "size": self.size,
            "supplier": self.supplier,
            "price": str(self.price),
            "quantity": self.quantity,
            "entry_date":self.entry_date,
            "expiry_date": self.expiry_date
        }


    @classmethod
    def from_dict(cls, data):
        return cls(
            product_id=data["product_id"],
            name=data["name"],
            price=data["price"],
            quantity=data["quantity"]
            category=data.get("cagetory", ""),
            brand=data.get("brand", ""),
            size=data.get("size", ""),
            supplier=data.get("supplier", ""),
            entry_date=data.get("entry_date"),
            expiry_date=data.get("expiry_date"))


    def __str__(self):
        return (f"[{self.product_id}] {self.name} | {self.brand} {self.size} | Price: {self.price} | Qty: {self.quantity} | Category: { self.category}")