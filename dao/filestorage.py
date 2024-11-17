import json
import os
from Model.product import Product
from dao.storage import Storage
from settings import Settings
from utility.saveimage import save_image

class FileStorage(Storage):
    def __init__(self, settings: Settings):
        self.settings = settings
        os.makedirs(os.path.dirname(self.settings.file_path), exist_ok=True)
        try:
            with open(self.settings.file_path, 'w') as file:
                json.dump([],file,indent=4)
        except Exception as e:
            print(f"An error Occured: {e}")

    def save(self, product: Product) -> None:
        product_dict = product.model_dump()
        try:
            with open(self.settings.file_path, 'r') as file:
                try:
                    data = json.load(file)
                except Exception as e:
                    print(f"An error Occured while loading the file: {e}")
                    data = []
            data.append(product_dict)

            with open(self.settings.file_path,'w') as file:
                try:
                    json.dump(data,file,indent=4)
                except Exception as e:
                    print(f"An error occured: {e}")
        except Exception as e:
            print(f"An error Occured: {e}")
        
        # Saving Images separately    
        self.__save_img(product=product)

    def __save_img(self, product: Product) -> None:
        img_url = product.product_image_url
        save_image(img_url, self.settings.img_path)