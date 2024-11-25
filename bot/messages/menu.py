from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from messages.base import BaseMessageBuilder


class MenuMessageBuilder(BaseMessageBuilder):
    _text = 'Тест'
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
