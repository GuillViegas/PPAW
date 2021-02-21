from requests import Session
from requests.exceptions import HTTPError

from .const import (
    POLONIEX_PUBLIC_URL,
    POLONIEX_WEBSOCKET_URL
)

from .exceptions import (
    CurrencyNotFound,
    CurrencyPairNotFound,
    PoloniexAPIException,
    PPAWException
)


class CurrencyPairs(dict):
    """ A custom dictionary to store currency pair infomation. """
    
    def __getitem__(self, key_pair: str) -> int:
        try:
            return super(CurrencyPairs, self).__getitem__(key_pair)
        except KeyError:
            return CurrencyPairNotFound(key_pair)

    def __repr__(self) -> str:
        return "\n".join([f'{self[key_pair]} - {key_pair}' for key_pair in self])


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

    _currencies = Currencies()
    _currency_pairs = CurrencyPairs()

    def __init__(self):
        self._public_url = POLONIEX_PUBLIC_URL
        self.session = Session()
        
        self._store_currencies()
        self._store_currency_pairs()

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

    @property
    def currencies(self) -> Currencies:
        return self._currencies

    @property
    def currency_pairs(self) -> CurrencyPairs:
        return self._currency_pairs

    def _store_currencies(self):
        """ Gets and stores information about currencies only if 
            there isn't this information. 
        """
        if not self._currencies:
            self._currencies = Currencies(self.return_currencies())

    def _store_currency_pairs(self):
        """ Gets and stores information about currency pairs only if 
            there isn't this information.     
        """
        if not self._currency_pairs:
            ticker = self.return_ticker()

            self._currency_pairs = CurrencyPairs({
                key_pair: ticker[key_pair]['id'] for key_pair in ticker
            })

    def return_currencies(self) -> Currencies:
        """  """
        return self._public('returnCurrencies')

    def return_ticker(self):
        """  """
        return self._public('returnTicker')
        

class PoloniexWebsocket:
    
    def __init__(self):
        self._websocket_url = POLONIEX_WEBSOCKET_URL


class Poloniex(PoloniexWebsocket, PoloniexPublic):
    pass