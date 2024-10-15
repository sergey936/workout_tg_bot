from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from messages.base import BaseMessageBuilder


class StartMessageBuilder(BaseMessageBuilder):
    _text = (
        "Привет, чтобы пользоваться этим ботом необходимо пройти регистрацию"
    )
    _reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Пройти регистрацию", callback_data="registration"
                )
            ]
        ]
    )
