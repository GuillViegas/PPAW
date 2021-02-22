def calculate_candle():
    trades = []

    def _aggregation_function(response_msg):
        if response_msg:
            for record in response_msg[2]:
                if record[0] == "t":
                        trades.append(record[3])

        if trades:
            return trades[0], max(trades), min(trades), trades[-1]

    return _aggregation_function