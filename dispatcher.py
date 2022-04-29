import logging
from aiogram import Bot, Dispatcher
import config


logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)
