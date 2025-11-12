from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    TELEGRAM_BOT_TOKEN: SecretStr
    
    REDIS_CONNECTION_URL: str
    DATABASE_CONNECTION_URL: str

settings = Settings()