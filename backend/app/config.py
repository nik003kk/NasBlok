from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator


class Settings(BaseSettings):
    """Nastavitve aplikacije, prebrane iz okolja ali datoteke .env."""

    database_url: str = "postgresql+psycopg://nasblok:nasblok@localhost:5432/nasblok"
    jwt_secret: str = "cc0efff385e38a140213ecf962bf8b281dadec02d93afe0e41daf3ec725121a8"
    jwt_expire_minutes: int = 480
    frontend_url: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @field_validator("database_url")
    @classmethod
    def normalize_database_url(cls, value: str) -> str:
        if value.startswith("postgresql://"):
            return value.replace("postgresql://", "postgresql+psycopg://", 1)
        return value


settings = Settings()