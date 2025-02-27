from dotenv import load_dotenv
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MONGODB_USERNAME: str
    MONGODB_PASSWORD: str
    MONGODB_NAME: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


load_dotenv()


settings = Settings()
