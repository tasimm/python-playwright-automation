from pydantic import BaseSettings

class Settings(BaseSettings):
    base_url: str
    username: str
    password: str
    timeout: int = 5000

    class Config:
        env_file = ".env"

settings = Settings()