from aiogram.filters.callback_data import CallbackData


class WorkoutCbData(CallbackData, prefix='workout-info'):
    workout_id: str