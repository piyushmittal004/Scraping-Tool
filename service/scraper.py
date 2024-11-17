import time
from bs4 import BeautifulSoup
import requests
from Model.product import Product
from Model.scrapeconfiguration import ScrapeConfiguration
from dao.dbstorage import DBStorage
from dao.filestorage import FileStorage
from settings import Settings
from utility.notifier.terminalnotifier import TerminalNotifier
from utility.saveimage import save_image

settings = Settings()


class Scraper:
    def scrape(self,scrape_configuration: ScrapeConfiguration) -> int:
        headers = settings.http_header
        proxies = {"http":scrape_configuration.proxy, "https":scrape_configuration.proxy} if scrape_configuration.proxy else None
        product_list:list[Product] = []

        for page in range(1,scrape_configuration.pages+1):
            flag:bool = False
            url = f"{scrape_configuration.url}/page/{page}"
            for _ in range(settings.retry_num):
                try:
                    response = requests.get(url, headers=headers, proxies=proxies, timeout = settings.http_timeout)
                    response.raise_for_status()
                    flag = True
                    break
                except requests.RequestException as e:
                    print(f"An error Occured: {e}")
                    time.sleep(3)
            if not flag:
                continue
            #print(response.text)
            soup = BeautifulSoup(response.text, "html.parser")
            #print(soup.prettify())
            products = soup.select(".product")
            print(len(products))
            for product in products:
                title = product.select_one(".woo-loop-product__title").text.strip()
                price = product.select_one(".woocommerce-Price-amount").text.replace("₹","").strip()
                #print(product.select_one("img").get("src"))
                img_url = product.select_one("img").get("data-lazy-src")
                print(title)
                print("Product End")
                img_dir = save_image(img_url, settings.img_path)
                new_product = Product(product_title=title, product_price=price, path_to_image=img_dir)
                product_list.append(new_product)
        
        if scrape_configuration.storage == "db" or scrape_configuration.storage == "both":
            storage = DBStorage()
            storage.save(products=product_list)
        
        if scrape_configuration.storage == "file" or scrape_configuration.storage == "both":
            storage = FileStorage()
            storage.save(products=product_list)

        products_scraped = len(product_list)
        notifier = TerminalNotifier()
        notifier.notify(products_scraped)

        return products_scraped
        


            