from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    first_name = State()
    second_name = State()
    email = State()
    password = State()
