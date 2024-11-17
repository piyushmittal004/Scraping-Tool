from Model.product import Product
from dao.storage import Storage
import sqlite3
from settings import Settings

class DBStorage(Storage):
    def __init__(self, settings:Settings):
        self.settings = settings
        self.conn = sqlite3.connect(self.settings.db_path)
        self.__initialize_table()
    
    def __initialize_table(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS products (
            product_name TEXT PRIMARY KEY,
            product_price REAL,
            path_to_image TEXT               
        )''')
        self.conn.commit()

    def save(self, product: Product) -> None:
        cursor = self.conn.cursor()
        cursor.execute('''
                INSERT OR REPLACE INTO products (product_title, product_price, path_to_image)
                VALUES (?,?,?)     
            ''', (product["product_title"], product["product_price"], product["path_to_image"]))
        self.conn.commit()

    