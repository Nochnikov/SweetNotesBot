from aiogram import Router
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bot_init import bot
from aiogram.filters import Command
from .sentenses import *
from loguru import logger
from random import randint
from dotenv import load_dotenv
from os import getenv

load_dotenv(dotenv_path=r"IndiBot/.env")

gr_chat_id = getenv("GRS_CHAT_ID")

router = Router()

chat_id_list = []

def get_random_number() -> int:
    return randint(0, 10)

@router.message(Command('start'))
async def start(message: Message):
    logger.info(f'START COMMAND INITIALIZED')
    await bot.send_message(
        chat_id=message.chat.id,
        text=start_command,
    )


@router.message(Command('help'))
async def help_(message: Message):
    logger.info(f'HELP COMMAND INITIALIZED')
    await bot.send_message(
        chat_id=message.chat.id,
        text=help_command
    )


@router.message(Command('us'))
async def us(message: Message):
    logger.info(f'US COMMAND INITIALIZED')
    await bot.send_message(
        chat_id=message.chat.id,
        text=us_command[get_random_number()]
    )


async def notification_on_time():
    try:
        await bot.send_message(chat_id=gr_chat_id, text=us_command[get_random_number()])
    except Exception as e:
        print(e)

scheduler = AsyncIOScheduler()
scheduler.add_job(notification_on_time, 'cron', hour=19, minute=00)
scheduler.start()









