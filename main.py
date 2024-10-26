import asyncio

from aiogram import Dispatcher
from notifications import notions
from bot_init import bot
from loguru import logger
app = Dispatcher()


app.include_router(notions.router)


async def main():
    logger.info("BOT START POLLING")
    await app.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())






