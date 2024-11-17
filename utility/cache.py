from Model.product import Product

class Cache:
    def __init__(self):
        self.cache:dict = {}
    def is_present_and_updated(self,product: Product) -> bool:
        if product.product_title not in self.cache:
            return False
        cached_product:Product = self.cache[product.product_title]
        return product.product_price == cached_product.product_price
    def update(self, product: Product) -> None:
        self.cache[product.product_title] = product
