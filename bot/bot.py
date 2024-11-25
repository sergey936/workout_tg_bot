import asyncio

from aiogram import Bot, Dispatcher

from containers.factories import get_container
from handlers.create_workout import router as create_workout_router

from handlers.start import router as start_router
from handlers.get_workouts import router as get_workout_router


async def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.include_router(router=start_router)
    dispatcher.include_router(router=get_workout_router)
    dispatcher.include_router(router=create_workout_router)


async def start_bot():
    container = get_container()
    bot, dp = await container.get(tuple[Bot, Dispatcher])
    await register_handlers(dispatcher=dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start_bot())
