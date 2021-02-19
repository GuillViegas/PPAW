from requests import Session
from requests.exceptions import HTTPError

from .const import POLONIEX_PUBLIC_URL
from .exceptions import (
    CurrencyNotFound,
    PoloniexAPIException,
    PPAWException
)


class Currencies(dict):
    """ A custom dictionary to store currency infomation. """

    def __getitem__(self, key: str) -> dict:
        try:
            return super(Currencies, self).__getitem__(key)
        except KeyError:
            raise CurrencyNotFound(key)

    def __repr__(self) -> str:
        currencies = [
            f'{self[currency]["id"]} - {self[currency]["name"]} ({currency})'
            for currency in self
        ]

        return "\n".join(currencies)


class PoloniexPublic:
    """ Provides convenient access to Poloniex's APIs.

    Instances of this class are the gateway to interacting with Poloniex's APIs
    though PPAW. An instance of this class can be obtained via:

    .. code-block:: python

        from ppaw import Poloniex

        poloniex = Poloniex()

    """

    currencies = Currencies()

    def __init__(self):
        self._public_url = POLONIEX_PUBLIC_URL
        self.session = Session()
        self._get_currencies()

    def _public(self, command: str, **params) -> dict:
        """ Invokes 'command' from Public HTTP Api.
        
        Available commands:
            - returnTicker
            - return24hVolume
            - returnOrderBooks
            - returnTradeHistory
            - returnChartData
            - returnCurrencies
            - returnLoanOrders

        """
        try:
            response = self.session.get(
                self._public_url,
                params={'command': command}
            )
            response.raise_for_status()
        except HTTPError as http_error:
            raise PoloniexAPIException(http_error)
        except Exception as error:
            raise PPAWException(error)

        return response.json()

    def _get_currencies(self):
        """ Gets and stores information about currencies only if 
            it doesn't have this information. 
        """
        if not self.currencies:
            self.currencies = Currencies(self._public('returnCurrencies'))
