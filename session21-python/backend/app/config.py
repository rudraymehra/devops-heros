from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

class Settings(BaseSettings):
    app_name: str = "CampusFix API"
    database_url: str | None = None
    pg_host: str = "localhost"
    pg_database: str = "taskboard"
    pg_user: str = "taskboard"
    pg_password: str = "taskboard"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def connection_url(self):
        return self.database_url or URL.create(
            "postgresql+psycopg", username=self.pg_user, password=self.pg_password,
            host=self.pg_host, port=5432, database=self.pg_database,
        )

settings = Settings()
