from typing import Iterable, Any

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from callbacks.workout import WorkoutCbData
from domain.dtos.workout import WorkoutDTO
from messages.base import BaseMessageBuilder


class WorkoutsListMessageBuilder(BaseMessageBuilder):
    def __init__(self, workouts: Iterable[WorkoutDTO]):
        self.workouts = workouts

    _text = 'Список тренировок'

    def build(self) -> Any | None:
        message = {
            'text': self._text,
            'reply_markup': InlineKeyboardMarkup(
                inline_keyboard=[
                    [InlineKeyboardButton(
                        text=workout.title,
                        callback_data=WorkoutCbData(workout_id=workout.id).pack())
                    ] for workout in self.workouts
                ],
            )
        }

        return message

