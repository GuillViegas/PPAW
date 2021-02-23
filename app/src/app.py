import asyncio
from db import engine, store_candle
from models import Base
from ppaw import PoloniexWebsocket
from ppaw.utils import calculate_candle
from sqlalchemy.orm import sessionmaker


base = Base()
base.metadata.create_all(engine)
conn = engine.connect()

p = PoloniexWebsocket()
asyncio.get_event_loop().run_until_complete(p.subscribe('USDC_BTC', calculate_candle, 60, store_candle))

