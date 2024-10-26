

from aiogram import Router
from aiogram.types import Message
from bot_init import bot
from aiogram.filters import Command
from .sentenses import *
from loguru import logger
from random import randint
router = Router()


def get_random_number() -> int:
    return randint(0, 10)

@router.message(Command('start'))
async def start(message: Message):
    logger.info(f'START COMMAND INITIALIZED')
    await bot.send_message(
        chat_id=message.chat.id,
        text=start_command)

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









