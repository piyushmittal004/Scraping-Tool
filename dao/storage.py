from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save(self, products: list[dict]):
        pass
