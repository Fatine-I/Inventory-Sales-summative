#Product base class
from abc import ABC, abstractmethod

class ProductBase(ABC):
    @abstractmethod
    def __init__(self):
        pass
    def display_details(self):
        pass