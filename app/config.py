import dotenv
import os

from pydantic import BaseSettings, Field, validator

dotenv.load_dotenv()

class Config(BaseSettings):
    APP_NAME: str = Field('mdau5h-notes', const=True)

    LOG_FILE: str
    HOST: str
    PORT: str

    @validator('LOG_FILE')
    def check_logfile_if_exists(cls, value):
        if not os.path.isfile(value):
            raise ValueError(f'Logfile {value!r} does not exists')
        return value

config = Config()
