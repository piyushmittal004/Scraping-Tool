from bs4 import BeautifulSoup, ResultSet
import requests
from Model.product import Product
from Model.scrapeconfiguration import ScrapeConfiguration
from dao.dbstorage import DBStorage
from dao.filestorage import FileStorage
from dao.storage import Storage
from settings import Settings
from utility.cache import Cache
from utility.notifier.notifier import Notifier
from utility.notifier.terminalnotifier import TerminalNotifier


class Scraper:
    def __init__(self):
        self.storage:Storage
        self.notifier:Notifier
        self.cache:Cache = Cache()
        self.settings:Settings = Settings()

    def scrape(self,scrape_configuration: ScrapeConfiguration) -> int:
        headers:dict = self.settings.http_header
        proxies:dict = {"http":scrape_configuration.proxy, "https":scrape_configuration.proxy} if scrape_configuration.proxy else None
        products_scraped:int = 0

        if scrape_configuration.storage == "db":
            self.storage = DBStorage(settings=self.settings)
                
        if scrape_configuration.storage == "file":
            self.storage = FileStorage(settings=self.settings)

        for page in range(1,scrape_configuration.pages+1):
            flag:bool = False
            url:str = f"{scrape_configuration.url}/page/{page}"
            for _ in range(self.settings.retry_num):
                try:
                    response = requests.get(url, headers=headers, proxies=proxies, timeout = self.settings.http_timeout)
                    response.raise_for_status()
                    flag = True
                    break
                except requests.RequestException as e:
                    print(f"An error Occured: {e}")
            if not flag:
                continue
            #print(response.text)
            soup:BeautifulSoup = BeautifulSoup(response.text, "html.parser")
            #print(soup.prettify())
            products:ResultSet = soup.select(".product")
            #print(len(products))
            for product in products:
                title:str = product.select_one(".woo-loop-product__title").text.strip()
                price:float = product.select_one(".woocommerce-Price-amount").text.replace("₹","").strip()
                #print(product.select_one("img").get("src"))
                img_url:str = product.select_one("img").get("data-lazy-src")
                #print(title)
                #print("Product End")
                new_product:Product = Product(product_title=title, product_price=price, product_image_url=img_url)
                if not self.cache.is_present_and_updated(new_product):
                    self.cache.update(product=new_product)
                    self.storage.save(product=new_product)
                    products_scraped += 1

        self.notifier = TerminalNotifier()
        self.notifier.notify(products_scraped)

        return products_scraped
        


            