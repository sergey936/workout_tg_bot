from dataclasses import dataclass

from exceptions.base import BaseWebException


@dataclass(frozen=True, eq=False)
class RegistrationRequestError(BaseWebException):

    @property
    def message(self):
        return "Registration error"


@dataclass(frozen=True, eq=False)
class GetTokenRequestError(BaseWebException):
    @property
    def message(self):
        return "Get token error"


@dataclass(frozen=True, eq=False)
class SetTelegramIDError(BaseWebException):
    @property
    def message(self):
        return "Set telegram id error"
