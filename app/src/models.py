from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import relationship


@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls):
        return 'candleapp_' + cls.__name__.lower()

    id = Column(Integer, primary_key=True)


class Candle(Base):
    currency_pair = Column(String(10), nullable=False)
    frequency = Column(String(10), nullable=False)
    created_at = Column(DateTime, nullable=False)
    open_value = Column(Float, nullable=False)
    low_value = Column(Float, nullable=False)
    high_value = Column(Float, nullable=False)
    close_value = Column(Float, nullable=False)
