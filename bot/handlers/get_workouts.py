from aiogram import Router, F, types

from containers.factories import get_container
from domain.use_cases.workouts import GetAllWorkoutsUseCase, GetAllWorkoutsCommand
from exceptions.base import BaseWebException
from messages.error import ErrorMessageBuilder
from messages.workout_list import WorkoutsListMessageBuilder

router = Router()


@router.message(F.text == 'Список тренировок')
async def get_all_workouts_message_handler(
        message: types.Message,
):
    container = get_container()

    async with container() as request_container:
        get_all_workouts_use_case: GetAllWorkoutsUseCase = await request_container.get(GetAllWorkoutsUseCase)

        try:
            workouts = await get_all_workouts_use_case.execute(
                GetAllWorkoutsCommand(
                    limit=10,
                    offset=0,
                    tg_id=message.from_user.id,
                )
            )
        except BaseWebException:
            await message.answer(**ErrorMessageBuilder().build())

    await message.answer(**WorkoutsListMessageBuilder(workouts).build())

