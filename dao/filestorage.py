import json
import os
from dao import storage
from settings import Settings

settings = Settings()

class FileStorage(storage):
    def save(self, products: list[dict]):
        os.makedirs(os.path.dirname(settings.file_path), exist_ok=True)
        with open(settings.file_path, 'w') as file:
            json.dump(products,file,indent=3)