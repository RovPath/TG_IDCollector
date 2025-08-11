import os
import asyncio
import logging
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv

from app.handlers import router as router_handlers


async def main():
    load_dotenv()
    bot = Bot(os.getenv("TG_TOKEN"))
    dp = Dispatcher()
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)
    dp.include_router(router_handlers)
    await dp.start_polling(bot)


async def startup(dispatcher: Dispatcher):
    print("Starting up...")


async def shutdown(dispatcher: Dispatcher):
    print("Shutting down...")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
