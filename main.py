from typing import Annotated
from fastapi import Depends, FastAPI

from Model.scrapeconfiguration import ScrapeConfiguration
import authentication

app = FastAPI()

@app.post("/scrape")
def scrape(scrape: ScrapeConfiguration, token: Annotated[str, Depends(authentication.authenticate)]):
    return scrape
