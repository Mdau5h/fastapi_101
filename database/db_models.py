from sqlalchemy import Column, BigInteger, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Note(Base):
    __tablename__ = "note"

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    title = Column(String)
    content = Column(String)