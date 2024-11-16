from Model.product import Product
from dao.storage import Storage
import sqlite3
from settings import Settings

settings = Settings()

class DBStorage(Storage):
    def __init__(self):
        self.conn = sqlite3.connect(settings.db_path)
        self.__initialize_table()
    
    def __initialize_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS products (
            product_name TEXT PRIMARY KEY,
            product_price REAL,
            path_to_image TEXT               
        )''')
        self.conn.commit()

    def save(self, products: list[Product]):
        cursor = self.conn.cursor()
        for product in products:
            cursor.execute('''
                INSERT OR REPLACE INTO products (product_title, product_price, path_to_image)
                VALUES (?,?,?)     
            ''', (product["product_title"], product["product_price"], product["path_to_image"]))
        self.conn.commit()

    