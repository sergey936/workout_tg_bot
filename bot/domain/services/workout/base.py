from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BaseWorkoutService(ABC):
    @abstractmethod
    async def create_workout(self, title: str, description: str) -> None:
        ...
