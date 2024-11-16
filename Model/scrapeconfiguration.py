from typing import Optional
from pydantic import BaseModel


class ScrapeConfiguration(BaseModel):
    pages: Optional[int] = 5
    proxy: Optional[str] = None
    url: Optional[str] = "https://dentalstall.com/shop/"
    storage: Optional[str] = "both" # "both", "db", "file"
