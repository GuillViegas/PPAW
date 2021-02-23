from collections import namedtuple
from datetime import datetime

candle_fields = ('currency_pair', 'frequency', 'datetime', 'open', 'low', 'high', 'close')
Candle = namedtuple('Candle', candle_fields, defaults=(None,) *len(candle_fields))


def calculate_candle(currency_pair, frequency):
    trades = []

    def _aggregation_function(response_msg):
        if response_msg and response_msg[0] != 1010:
            for record in response_msg[2]:
                if record[0] == "t":
                        trades.append(record[3])

        if trades:
            return Candle(currency_pair, f'{frequency} min', datetime.now(), trades[0], min(trades), max(trades), trades[-1])

        return Candle()

    return _aggregation_function