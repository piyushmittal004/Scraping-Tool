from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    token: str = "somestatictoken"
    auth_scheme: str = "bearer"
    db_path:str = "path_to_db"