import dotenv
import os

from pydantic import BaseSettings, Field, validator

dotenv.load_dotenv()

class Config(BaseSettings):
    APP_NAME: str = Field('mdau5h-notes', const=True)

    LOG_FILE: str
    HOST: str
    PORT: str

    DB_PG_HOST: str
    DB_MASTER_PG_PORT: int
    DB_PG_USERNAME: str
    DB_PG_PASSWORD: str
    DB_PG_BASENAME: str

    @property
    def DB_PG_URL(self, db_name):
        return 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'.format(
            user=self.DB_PG_USERNAME,
            password=self.DB_PG_PASSWORD,
            host=self.DB_PG_HOST,
            port=self.DB_MASTER_PG_PORT,
            db_name=self.DB_PG_BASENAME,
        )

    @validator('LOG_FILE')
    def check_logfile_if_exists(cls, value):
        if not os.path.isfile(value):
            raise ValueError(f'Logfile {value!r} does not exists')
        return value

config = Config()
