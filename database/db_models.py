import datetime
from sqlalchemy import Column, BigInteger, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base, declarative_mixin


Base = declarative_base()

@declarative_mixin
class BaseMixin:
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    deleted = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime, nullable=False,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow
    )

class Note(BaseMixin, Base):
    __tablename__ = 'note'

    id = Column(BigInteger, autoincrement=True, primary_key=True)
    title = Column(String(50), default='')
    content = Column(String(255), default='')