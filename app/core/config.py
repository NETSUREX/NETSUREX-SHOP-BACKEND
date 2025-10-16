from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    APP_NAME: str = "NetSurex Shop API"
    APP_VERSION: str = "1.0.0"
    DATABASE_URL: str = "sqlite:///./netsurex_shop.db"
    API_PREFIX: str = "/api"
    SECRET_KEY: str = "tu_clave_secreta_muy_segura_aqui"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()