import asyncio

from aiogram import Dispatcher, Bot

from containers.factories import get_container
from handlers.start import router as start_router


async def register_handlers(dispatcher: Dispatcher) -> None:
    dispatcher.include_router(router=start_router)


async def start_bot():
    container = get_container()
    bot, dp = await container.get(Bot)
    await register_handlers(dispatcher=dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_bot())
