from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from messages.base import BaseMessageBuilder


class MenuMessageBuilder(BaseMessageBuilder):
    _text = 'Тест'
    _reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text='Создать тренировку', callback_data='test',
                ),
                KeyboardButton(
                    text='Обновить тренировку', callback_data='test',
                ),
                KeyboardButton(
                    text='Удалить тренировку', callback_data='test',
                ),
                KeyboardButton(
                    text='Посмотреть список моих тренировок',
                    callback_data='test',
                ),
            ],
        ],
        resize_keyboard=True,
    )
