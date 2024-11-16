from abc import ABC, abstractmethod

from Model.product import Product

class Storage(ABC):
    @abstractmethod
    def save(self, products: list[Product]):
        pass