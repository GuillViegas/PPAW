from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Candle

from config import DB_URI

engine = create_engine(DB_URI)

async def store_candle(candle):
    Session = sessionmaker(engine)
    session = Session()

    candle = Candle(currency_pair=candle.currency_pair, frequency=candle.frequency,
        created_at=candle.datetime, open_value=candle.open,
        low_value=candle.low, high_value=candle.high,
        close_value=candle.close
    )

    session.add(candle)
    session.commit()
    session.close()

