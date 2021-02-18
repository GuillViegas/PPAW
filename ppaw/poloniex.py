from requests import Session

from .const import POLONIEX_PUBLIC_URL
from .exceptions import (
    CurrencyNotFound
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

        return "\n".join(sorted(currencies))


class PoloniexPublic:
    """ Provides convenient access to Poloniex's APIs.

    Instances of this class are the gateway to interacting with Poloniex's APIs
    though PPAW. An instance of this class can be obtained via:

    .. code-block:: python

        from ppaw import Poloniex

        poloniex = Poloniex()

    """

    __currencies = None

    def __init__(self):
        self._public_url = POLONIEX_PUBLIC_URL
        self.session = Session()

    def _public(self, command: str) -> dict:
        """ """

        return self.session.get(
            self._public_url,
            params={'command': command}
        ).json()

    @property
    def currencies(self):
        """ A property that returns an Currencies object (a dictionary) with
            all available currencies.
        """

        if not self.__currencies:
            self.__currencies = Currencies(self._public('returnCurrencies'))

        return self.__currencies
