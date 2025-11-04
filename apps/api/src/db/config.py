from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="POSTGRES_",
        extra="ignore",
    )

    USERNAME: str
    PASSWORD: str
    HOST: str
    PORT: int
    DB_NAME: str

