from aiogram.fsm.state import State, StatesGroup


class CreateWorkout(StatesGroup):
    title = State()
    description = State()
    file = State()
