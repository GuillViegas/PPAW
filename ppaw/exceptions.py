""" PPAW exception classes. """


class PPAWException(Exception):
    """ The base PPAW Exception that all other exception classes extend. """


class ClientException(PPAWException):
    """ Indicates an exception that involving the client """


class CurrencyNotFound(ClientException):
    """ Indicates an exceptions when trying to access a position that does not
        exist in the currency list.
    """

    def __init__(self, key: str):
        super().__init__(f"The currency key {key} was not found.")