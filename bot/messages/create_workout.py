from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from messages.base import BaseMessageBuilder


class CreateWorkoutMessageBuilder(BaseMessageBuilder):
    _text = 'Тренировка создана'
    _reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text='Создать тренировку',
                ),
                KeyboardButton(
                    text='Список тренировок',
                ),
            ],
            [
                KeyboardButton(
                    text='Посмотреть список моих тренировок',
                ),
            ],
        ],
        resize_keyboard=True,
    )

