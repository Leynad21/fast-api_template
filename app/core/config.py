from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Book Collection API"
    secret_key: str  # Populated from the .env file
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Database configurations
    db_name: str
    db_username: str
    db_password: str
    db_host: str = "localhost"
    db_port: str = "5432"

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"


settings = Settings()
