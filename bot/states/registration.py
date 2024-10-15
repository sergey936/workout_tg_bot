from aiogram.fsm.state import StatesGroup, State


class Registration(StatesGroup):
    first_name = State()
    second_name = State()
    email = State()
    password = State()
