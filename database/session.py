from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import config


def session_factory():
    engine = create_engine(config.DB_PG_URL, echo=True)
    db_session = sessionmaker(bind=engine)
    return db_session()
