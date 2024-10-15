from dataclasses import dataclass

from domain.services.workout.base import BaseWorkoutService


@dataclass
class WebWorkoutService(BaseWorkoutService):
    async def create_workout(self) -> None:
        ...