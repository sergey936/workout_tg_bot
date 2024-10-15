from aiogram import F, Router
from aiogram import types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from containers.factories import get_container

from domain.dtos.user import UserDTO
from domain.use_cases.user import (
    CheckTGUserExistsCommand,
    CheckTGUserExistsUseCase,
    RegistrationUseCase,
    RegistrationUserCommand,

)

from exceptions.base import BaseWebException

from messages.menu import MenuMessageBuilder
from messages.start import StartMessageBuilder

from states.registration import Registration

router = Router()


@router.message(CommandStart())
async def start_command_handler(message: types.Message):
    container = get_container()

    async with container() as request_container:
        registration_use_case: RegistrationUseCase = (
            await request_container.get(CheckTGUserExistsUseCase)
        )

        user_exists = await registration_use_case.execute(
            CheckTGUserExistsCommand(
                    tg_id=message.from_user.id,
            ),
        )

    if user_exists:
        content = MenuMessageBuilder().build()
    else:
        content = StartMessageBuilder().build()
    return await message.answer(**content)


@router.callback_query(F.data == 'registration')
async def start_registration_callback_handler(
    callback: types.CallbackQuery, state: FSMContext,
):
    await callback.answer()
    await state.set_state(Registration.first_name)
    await state.update_data(tg_id=callback.from_user.id)
    await callback.message.answer('Введите ваше имя')


@router.message(Registration.first_name)
async def registration_get_first_name_command_handler(
    message: types.Message, state: FSMContext,
):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration.second_name)
    await message.answer('Введите вашу фамилию')


@router.message(Registration.second_name)
async def registration_get_second_name_command_handler(
    message: types.Message, state: FSMContext,
):
    await state.update_data(second_name=message.text)
    await state.set_state(Registration.email)
    await message.answer('Введите вашу почту')


@router.message(Registration.email)
async def registration_get_email_command_handler(
    message: types.Message, state: FSMContext,
):
    await state.update_data(email=message.text)
    await state.set_state(Registration.password)
    await message.answer('Введите ваш пароль')


@router.message(Registration.password)
async def complete_registration_command_handler(
    message: types.Message, state: FSMContext,
):
    container = get_container()

    async with container() as request_container:
        registration_use_case: RegistrationUseCase = (
            await request_container.get(RegistrationUseCase)
        )

        await state.update_data(password=message.text)
        data = await state.get_data()
        try:
            await registration_use_case.execute(
                RegistrationUserCommand(
                    user=UserDTO(
                        **data,
                    ),
                ),
            )

        except BaseWebException as err:
            await message.answer(
                f'Ошибка во время регистрации: {err.error_text}',
            )
        else:
            await message.answer(
                f'Регистрация завершена: {await state.get_data()}',
            )

        await state.clear()


@router.message(F.text)
async def all_non_commands_text_handler(message: types.Message):
    await message.answer('Я не знаю такую команду')
