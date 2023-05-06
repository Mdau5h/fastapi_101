from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from app.config import config


engine = create_engine(config.DB_PG_URL, echo=True)

def session_factory() -> Session:
    db_session = sessionmaker(engine)
    with db_session() as session:
        return session
