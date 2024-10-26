from dotenv import load_dotenv
from os import getenv
from aiogram import Bot

load_dotenv()
TOKEN = getenv('TOKEN')


bot = Bot(token=TOKEN)

