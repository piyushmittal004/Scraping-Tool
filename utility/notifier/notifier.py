from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def notify(self, products_scraped: int) -> None:
        pass