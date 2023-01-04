import dotenv

from pydantic import BaseSettings, Field


dotenv.load_dotenv()


class Config(BaseSettings):
    APP_NAME: str = Field('mdau5h-notes', const=True)

config = Config()
