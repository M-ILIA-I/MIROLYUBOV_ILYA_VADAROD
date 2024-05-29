from sqlalchemy.orm import as_declarative, relationship, Mapped
from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, JSON
from sqlalchemy.orm import declarative_base


@as_declarative()
class Base:
    """Базовая модель."""
    __name__: str


al_base = declarative_base()


class CurrencyRate(Base):
    __tablename__ = 'currency_rates'

    date = Column(String, primary_key=True)
    data = Column(JSON, nullable=False)
