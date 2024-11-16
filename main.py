from typing import Annotated
from fastapi import Depends, FastAPI

from Model.scrapeconfiguration import ScrapeConfiguration
import authentication
from service.scraper import Scraper

app = FastAPI()
scraper = Scraper()

@app.post("/scrape")
def scrape(scrape_conf: ScrapeConfiguration, token: Annotated[str, Depends(authentication.authenticate)]):
    return scraper.scrape(scrape_conf)
