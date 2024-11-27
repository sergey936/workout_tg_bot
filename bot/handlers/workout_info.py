from aiogram import Router, types

from callbacks.workout import WorkoutCbData
from containers.factories import get_container
from domain.use_cases.workouts import GetWorkoutUseCase, GetWorkoutCommand
from messages.workout_info import WorkoutInfoMessageBuilder


router = Router()

@router.callback_query(
    WorkoutCbData.filter(),
)
async def workout_info_callback_handler(
        callback: types.CallbackQuery,
        callback_data: WorkoutCbData,
):
    container = get_container()

    async with container() as request_container:
        get_workout_use_case: GetWorkoutUseCase = (
            await request_container.get(GetWorkoutUseCase)
        )
    workout = await get_workout_use_case.execute(
        GetWorkoutCommand(
            workout_id=callback_data.workout_id,
            tg_id=callback.from_user.id,
        )
    )

    await callback.answer()
    await callback.message.answer(**WorkoutInfoMessageBuilder(workout=workout).build())
