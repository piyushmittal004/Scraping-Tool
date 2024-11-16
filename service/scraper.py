import time
from bs4 import BeautifulSoup
import requests
from Model.product import Product
from Model.scrapeconfiguration import ScrapeConfiguration
from settings import Settings

settings = Settings()


class Scraper:
    def scrape(self,scrape_configuration: ScrapeConfiguration) -> int:
        headers = settings.http_header
        proxies = {"http":scrape_configuration.proxy, "https":scrape_configuration.proxy} if scrape_configuration.proxy else None
        products_count = 0

        for page in range(1,scrape_configuration.pages+1):
            flag:bool = False
            url = f"{scrape_configuration.url}/page/{page}"
            for _ in range(settings.retry_num):
                try:
                    response = requests.get(url, headers=headers, proxies=proxies, timeout = settings.http_timeout)
                    response.raise_for_status()
                    flag = True
                    break
                except requests.RequestException:
                    time.sleep(3)
            if not flag:
                continue
            #print(response.text)
            soup = BeautifulSoup(response.text, "html.parser")
            #print(soup.prettify())
            products = soup.select(".products")
            #print(products)

            