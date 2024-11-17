from utility.notifier.notifier import Notifier


class TerminalNotifier(Notifier):
    def notify(self, products_scraped: int) -> None:
        print(f"{products_scraped} products scraped")