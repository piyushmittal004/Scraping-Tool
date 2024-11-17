from typing import Optional
from pydantic import BaseModel


class ScrapeConfiguration(BaseModel):
    pages: Optional[int] = 3
    proxy: Optional[str] = None
    url: Optional[str] = "https://dentalstall.com/shop"
    storage: Optional[str] = "file" # "db", "file"
