from aiogram import Router, F, types, Dispatcher, Bot
from aiogram.fsm.context import FSMContext

from containers.factories import get_container
from domain.use_cases.workouts import CreateWorkoutUseCase, CreateWorkoutCommand
from exceptions.base import BaseWebException
from messages.create_workout import CreateWorkoutMessageBuilder
from messages.error import ErrorMessageBuilder
from states.create_workout import CreateWorkout

router = Router()


@router.message(F.text == 'Создать тренировку')
async def create_workout_message_handler(
        message: types.Message, state: FSMContext,
):
    await state.set_state(CreateWorkout.title)

    await message.answer('Введите название для тренировки')


@router.message(CreateWorkout.title)
async def create_workout_get_title_message_handler(
    message: types.Message, state: FSMContext,
):
    await state.update_data(title=message.text)
    await state.set_state(CreateWorkout.description)

    await message.answer('Введите описание для тренировки')


@router.message(CreateWorkout.description)
async def create_workout_get_description_message_handler(
    message: types.Message, state: FSMContext,
):
    await state.update_data(description=message.text)
    await state.set_state(CreateWorkout.file)

    await message.answer('Загрузите файл для тренировки')


@router.message(CreateWorkout.file)
async def create_workout_get_file_message_handler(
    message: types.Message, state: FSMContext,
):
    container = get_container()

    bot, dp = await container.get(tuple[Bot, Dispatcher])

    if message.photo:
        file_id = message.photo[-1].file_id
    elif message.document:
        file_id = message.document.file_id

    async with container() as request_container:
        create_workout_use_case: CreateWorkoutUseCase = await request_container.get(
            CreateWorkoutUseCase
        )

        file_info = await bot.get_file(file_id)
        file_path = file_info.file_path
        file_format = file_path.split('.')[1]

        io_file = await bot.download_file(file_path)
        data = await state.get_data()

        try:
            await create_workout_use_case.execute(
                CreateWorkoutCommand(
                    title=data['title'],
                    description=data['description'],
                    file=io_file,
                    tg_id=message.from_user.id,
                    file_format=file_format,
                )
            )
        except BaseWebException as err:
            await message.answer(**ErrorMessageBuilder().build())
        else:
            await message.answer(**CreateWorkoutMessageBuilder().build())

    await state.clear()


@router.message(F.text)
async def all_non_commands_text_handler(message: types.Message):
    await message.answer(f'Я не знаю такую команду: {message.text}')
