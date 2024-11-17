import json
import os
from Model.product import Product
from dao.storage import Storage
from settings import Settings

settings = Settings()

class FileStorage(Storage):
    def save(self, products: list[Product]):
        product_dict = [product.model_dump() for product in products]
        os.makedirs(os.path.dirname(settings.file_path), exist_ok=True)
        with open(settings.file_path, 'w') as file:
            json.dump(product_dict,file,indent=4)