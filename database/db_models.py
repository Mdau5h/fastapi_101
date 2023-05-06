from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Note(Base):
    __tablename__ = 'note'

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    title = Column(String(50), default='')
    content = Column(String(255), default='')