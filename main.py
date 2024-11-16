from fastapi import FastAPI
from Model.scrapeconfiguration import ScrapeConfiguration

app = FastAPI()

@app.post("/scrape")
def scrape(scrape: ScrapeConfiguration):
    return scrape
