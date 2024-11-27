from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from messages.base import BaseMessageBuilder


class RegistrationCompleteMessageBuilder(BaseMessageBuilder):
    _text = 'Регистрация завершена'
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