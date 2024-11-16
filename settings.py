from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    token: str = "somestatictoken"
    auth_scheme: str = "bearer"
    db_path:str = "path_to_db"
    file_path:str = "path_to_storage"
    retry_num:int = 3
    http_header:dict = {"user-Agent": "Mozzila/5.0"}
    http_timeout:int = 10