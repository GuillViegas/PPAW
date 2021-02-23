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

With the ``poloniex``instance you can then interact with Poloniex:

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
    {'id': 28, 'name': 'Bitcoin', 'humanType': 'BTC Clone', 'currencyType': 'address', 'txFee': '0.00050000', 'minConf': 1, 
    'depositAddress': None, 'disabled': 0, 'frozen': 0, 'hexColor': 'F59C3D', 'blockchain': 'BTC', 'delisted': 0, 'isGeofen
    ced': 0}
