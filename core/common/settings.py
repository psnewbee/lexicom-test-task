from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Notebook"
    API_PREFIX: str = "/api"
    DOCS_URL: str = "/docs"

    REDIS_PASSWORD: str
    REDIS_HOST: str
    REDIS_PORT: int

    class Config:
        case_sensitive = True


settings: Settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
