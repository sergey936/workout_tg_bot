from typing import Any

from domain.dtos.workout import WorkoutDTO
from messages.base import BaseMessageBuilder


class WorkoutInfoMessageBuilder(BaseMessageBuilder):
    def __init__(self, workout: WorkoutDTO):
        self.workout = workout


    def build(self) -> Any | None:
        message = {
            'text': f'Тренировка: {self.workout.title}\nОписание: {self.workout.description}\nФайл: {self.workout.file_path}',
        }

        return message
