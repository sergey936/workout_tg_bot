from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseUserService(ABC):
    @abstractmethod
    async def create_user(
        self,
        email: str,
        password: str,
        first_name: str,
        second_name: str,
        patronymic: str,
    ) -> None: ...

    @abstractmethod
    async def get_token(
        self,
        email: str,
        password: str,
    ) -> str: ...

    @abstractmethod
    async def set_tg_id(
        self,
        token: str,
        tg_id: str,
    ) -> None: ...

    @abstractmethod
    async def check_tg_user_exists(self, tg_id: str) -> bool:
        ...
