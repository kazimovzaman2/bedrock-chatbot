from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    AWS_ACCESS_KEY: str
    AWS_SECRET_KEY: str
    AWS_REGION: str
    BEDROCK_MODEL_ID: str

    class Config:
        env_file = ".env"


settings = Settings()
