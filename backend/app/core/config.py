from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    SECRET_KEY: str = Field("super-secret-key", env="SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(60 * 24)  # 1 day
    DATABASE_HOST: str = Field("database")
    DATABASE_PORT: int = Field(3306)
    DATABASE_USER: str = Field("xtreamcodes")
    DATABASE_PASSWORD: str = Field("xtream123")
    DATABASE_NAME: str = Field("xstream_codes")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

settings = Settings()