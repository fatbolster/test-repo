from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "My API"
    debug: bool = False

    class Config:
        env_file = ".env"


def get_settings() -> Settings:
    return Settings()
