from database.session import engine
from database.db_models import Base

def db_setup():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
