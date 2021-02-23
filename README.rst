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
You need to provide a currency pair key, like 'USDC_BTC', an aggregation function, in this
case a closure that calculates a candle(opening, minimum, maximun and closing value) for a
period of time, the corresponding period, and a callback function that will consume the values.

.. code-block:: python

    import asyncio
    from db import store_candle
    from ppaw import Poloniex
    from ppaw.utils import calculate_candle

    p = Poloniex()
    asyncio.get_event_loop().run_until_complete(p.subscribe('USDC_BTC', calculate_candle, 60, store_candle))