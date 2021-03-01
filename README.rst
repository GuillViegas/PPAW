PPAW: Python Poloniex API Wrapper
===================================

PPAW, an acronym for "Python Poloniex API Wrapper", is a Python package that allows for simple access to Poloniex's API.

.. _installation:

Installation
------------

This project is dockerized, so it can be run using the command **docker-compose up**. However, 
if your only intention is just use the wrapper, you can install the library using the following
command:

.. code-block:: bash

    $ pip install ppaw/

Quickstart
----------

Poloniex's instances provide a facade to access both the Public and Websocket APIs. An instance of this class can be
obtained via:

.. code-block:: Python

    from ppaw import Poloniex
    poloniex = Poloniex()

With the ``poloniex`` instance you can then interact with Poloniex:

.. code-block:: python

    # List currencies
    >>>> poloniex.currencies
    1 - 1CRedit (1CR)
    446 - Aave (AAVE)
    2 - ArtByte (ABY)
    3 - AsiaCoin (AC)
    4 - Altcoin Herald (ACH)
    ...

    # Return information about currency
    >>>> poloniex.currencies['BTC'] 
    {'id': 28, 'name': 'Bitcoin', 'humanType': 'BTC Clone', 'currencyType': 'address', 
    'txFee': '0.00050000', 'minConf': 1, 'depositAddress': None, 'disabled': 0, 'froze
    n': 0, 'hexColor': 'F59C3D', 'blockchain': 'BTC', 'delisted': 0, 'isGeofenced': 0}

    # List currency pairs
    >>>> poloniex.currency_pairs
    14 - BTC_BTS
    24 - BTC_DASH
    27 - BTC_DOGE
    50 - BTC_LTC
    69 - BTC_NXT
    ...

    # Returns the currency pair id
    >>>> poloniex.currency_pairs['USDC_BTC']
    224


Usage Examples
--------------

Subscribe Method
""""""""""""""""

This is an asynchronous method that establishes a connection with the poloniex websocket. 
You need to provide a currency pair key, like *USDC_BTC*, an aggregation function, in this
case a closure that calculates a candle(opening, minimum, maximun and closing value) for a
period of time, the corresponding period, in seconds, and a callback function that will consume 
the values.

.. code-block:: python

    import asyncio
    from db import store_candle
    from ppaw import Poloniex
    from ppaw.utils import calculate_candle

    p = Poloniex()
    asyncio.get_event_loop().run_until_complete(p.subscribe('USDC_BTC', calculate_candle, 
    60, store_candle))


Docker App
""""""""""

The app can be run using the command **docker-compose up**. It will go up two containers, 
a mysql and a python container. The mysql container needs to be running and receiving requests 
for the application to work. The python application will save the aggregated data every minute.
This can be changed by modifying the third paramenter of the subscribe method.

To access the mysql containers and see the latest records, you can use the following command:

.. code-block:: bash

    $ docker exec -it <mysql_container_id> sh

To acess the database:

.. code-block:: bash

    $ mysql -h 127.0.0.1 -u candles_app --password=Y2FuZGxlc19hcHA=

Finally, to list the latest records:

.. code-block:: sql

    mysql> SELECT * FROM candles_db.candleapp_candle;
    +----+---------------+-----------+---------------------+------------+-----------+------------+-------------+
    | id | currency_pair | frequency | created_at          | open_value | low_value | high_value | close_value |
    +----+---------------+-----------+---------------------+------------+-----------+------------+-------------+
    |  1 | USDC_BTC      | 1.0 min   | 2021-03-01 16:46:39 |    48960.9 |   48836.7 |    48965.9 |     48861.3 |
    |  2 | USDC_BTC      | 1.0 min   | 2021-03-01 16:47:39 |    48782.7 |   48782.7 |      48800 |       48800 |
    |  3 | USDC_BTC      | 1.0 min   | 2021-03-01 16:48:39 |    48814.4 |   48714.3 |    48814.4 |     48775.5 |
    |  4 | USDC_BTC      | 1.0 min   | 2021-03-01 16:49:39 |    48785.7 |   48714.3 |      48802 |     48714.3 |
    |  5 | USDC_BTC      | 1.0 min   | 2021-03-01 16:50:39 |    48726.6 |   48634.4 |    48726.6 |       48659 |
    |  6 | USDC_BTC      | 1.0 min   | 2021-03-01 16:52:39 |    48652.6 |   48652.6 |      48853 |     48786.2 |
    |  7 | USDC_BTC      | 1.0 min   | 2021-03-01 16:53:40 |    48821.5 |   48775.5 |    48836.7 |     48799.7 |
    |  8 | USDC_BTC      | 1.0 min   | 2021-03-01 16:54:40 |    48836.7 |   48836.7 |    48866.9 |     48866.9 |
    |  9 | USDC_BTC      | 1.0 min   | 2021-03-01 16:55:40 |      48898 |     48898 |    48959.2 |     48959.2 |
    | 10 | USDC_BTC      | 1.0 min   | 2021-03-01 16:56:40 |      48898 |   48893.4 |    49142.9 |     49142.9 |
    | 11 | USDC_BTC      | 1.0 min   | 2021-03-01 16:57:40 |    49204.1 |   49142.9 |    49324.1 |     49148.7 |
    | 12 | USDC_BTC      | 1.0 min   | 2021-03-01 16:58:40 |    49265.3 |   49204.1 |    49265.3 |     49204.1 |
    | 13 | USDC_BTC      | 1.0 min   | 2021-03-01 16:59:40 |    49204.1 |   49200.5 |    49204.1 |     49200.5 |
    | 14 | USDC_BTC      | 1.0 min   | 2021-03-01 17:00:40 |    49173.5 |   49097.3 |    49173.5 |     49144.9 |
    | 15 | USDC_BTC      | 1.0 min   | 2021-03-01 17:01:40 |    49120.5 |   49120.5 |    49120.5 |     49120.5 |
    | 16 | USDC_BTC      | 1.0 min   | 2021-03-01 17:02:40 |    49172.8 |   49172.8 |    49172.8 |     49172.8 |
    | 17 | USDC_BTC      | 1.0 min   | 2021-03-01 17:03:40 |    49187.9 |   49187.9 |    49265.3 |     49204.1 |
    | 18 | USDC_BTC      | 1.0 min   | 2021-03-01 17:04:40 |    49142.9 |   49081.6 |    49142.9 |     49081.6 |
    | 19 | USDC_BTC      | 1.0 min   | 2021-03-01 17:05:40 |    49037.7 |   49037.7 |    49204.1 |     49204.1 |
    | 20 | USDC_BTC      | 1.0 min   | 2021-03-01 17:06:41 |      49167 |   49103.3 |      49167 |     49142.6 |
    | 21 | USDC_BTC      | 1.0 min   | 2021-03-01 17:07:41 |    49081.6 |   49081.6 |    49084.3 |     49084.3 |
    | 22 | USDC_BTC      | 1.0 min   | 2021-03-01 17:08:41 |    49142.9 |   49142.9 |    49142.9 |     49142.9 |
    | 23 | USDC_BTC      | 1.0 min   | 2021-03-01 17:09:41 |    49182.6 |   49133.5 |    49182.6 |     49133.5 |
    | 24 | USDC_BTC      | 1.0 min   | 2021-03-01 17:10:41 |    49081.6 |     49071 |    49082.4 |     49082.4 |
    | 25 | USDC_BTC      | 1.0 min   | 2021-03-01 17:11:41 |    49101.3 |   49101.3 |    49145.2 |     49145.2 |
    | 26 | USDC_BTC      | 1.0 min   | 2021-03-01 17:12:41 |    49113.6 |   49042.8 |    49113.6 |     49042.8 |
    | 27 | USDC_BTC      | 1.0 min   | 2021-03-01 17:13:41 |      49025 |     49025 |    49075.9 |     49074.9 |
    | 28 | USDC_BTC      | 1.0 min   | 2021-03-01 17:14:41 |    49050.5 |   49020.4 |    49050.5 |     49020.4 |
    | 29 | USDC_BTC      | 1.0 min   | 2021-03-01 17:15:42 |    49000.5 |     48898 |    49000.5 |       48898 |
    | 30 | USDC_BTC      | 1.0 min   | 2021-03-01 17:16:42 |    48883.6 |   48818.1 |    48883.6 |     48818.1 |
    | 31 | USDC_BTC      | 1.0 min   | 2021-03-01 17:17:42 |    48840.1 |   48840.1 |    48840.1 |     48840.1 |
    | 32 | USDC_BTC      | 1.0 min   | 2021-03-01 17:18:42 |      48898 |     48898 |    48904.6 |     48904.6 |
    | 33 | USDC_BTC      | 1.0 min   | 2021-03-01 17:19:42 |      48896 |     48896 |      48922 |     48899.5 |
    | 34 | USDC_BTC      | 1.0 min   | 2021-03-01 17:20:42 |    48922.9 |   48922.9 |    48959.2 |     48959.2 |
    | 35 | USDC_BTC      | 1.0 min   | 2021-03-01 17:21:42 |    48934.1 |   48836.7 |    48934.1 |     48842.2 |
    | 36 | USDC_BTC      | 1.0 min   | 2021-03-01 17:22:42 |      48898 |     48898 |    48959.2 |     48959.2 |
    | 37 | USDC_BTC      | 1.0 min   | 2021-03-01 17:23:43 |    48959.6 |   48957.9 |    48959.6 |     48957.9 |
    | 38 | USDC_BTC      | 1.0 min   | 2021-03-01 17:24:43 |    48994.5 |   48913.7 |    48994.5 |     48913.7 |
    | 39 | USDC_BTC      | 1.0 min   | 2021-03-01 17:25:43 |    48919.6 |     48890 |    48919.6 |       48890 |
    | 40 | USDC_BTC      | 1.0 min   | 2021-03-01 17:26:43 |    48941.1 |   48941.1 |    48959.2 |       48949 |
    | 41 | USDC_BTC      | 1.0 min   | 2021-03-01 17:27:43 |    48960.3 |   48922.2 |    48974.4 |     48922.2 |
    | 42 | USDC_BTC      | 1.0 min   | 2021-03-01 17:28:43 |    48950.1 |     48898 |    48950.1 |       48898 |
    | 43 | USDC_BTC      | 1.0 min   | 2021-03-01 17:29:43 |      48958 |     48958 |    49081.6 |     49081.6 |
    | 44 | USDC_BTC      | 1.0 min   | 2021-03-01 18:02:41 |    48723.8 |   48723.8 |    48753.8 |     48753.8 |
    | 45 | USDC_BTC      | 1.0 min   | 2021-03-01 18:03:41 |    48775.5 |   48714.3 |    48775.5 |     48737.2 |
    | 46 | USDC_BTC      | 1.0 min   | 2021-03-01 18:04:41 |    48775.5 |   48775.5 |    48815.5 |     48815.5 |
    +----+---------------+-----------+---------------------+------------+-----------+------------+-------------+
    46 rows in set (0.02 sec)
