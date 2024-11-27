from abc import ABC, abstractmethod
from collections.abc import Iterable
from dataclasses import dataclass
from io import BytesIO
from typing import Any

from domain.dtos.workout import WorkoutDTO


@dataclass
class BaseWorkoutService(ABC):
    @abstractmethod
    async def create_workout(self, title: str, description: str, tg_id: int) -> dict[str, Any]:
        ...

    @abstractmethod
    async def get_all_workouts(self, limit: int, offset: int, tg_id: int) -> Iterable[WorkoutDTO] | None:
        ...

    @abstractmethod
    async def upload_workout_file(self, file: BytesIO, workout_id: str, tg_id: int, file_format: str) -> None:
        ...

    @abstractmethod
    async def get_workout_info(self, workout_id: str, tg_id: int) -> WorkoutDTO:
        ...
