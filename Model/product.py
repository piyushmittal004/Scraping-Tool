from pydantic import BaseModel

class Product(BaseModel):
    product_title: str
    product_price: float
    product_image_url: str