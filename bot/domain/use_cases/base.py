from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Generic, TypeVar

C = TypeVar("C")
R = TypeVar("R")


@dataclass
class BaseUseCase(ABC, Generic[C, R]):

    @abstractmethod
    async def execute(self, command: C) -> R: ...
