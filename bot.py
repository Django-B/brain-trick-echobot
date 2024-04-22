import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

API_TOKEN = os.getenv('BOT_TOKEN')
assert API_TOKEN, 'missing BOT_TOKEN environment variable'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Привет!")



@dp.message_handler()
async def echo(message: types.Message):
    text = 'Отлично, давай еще одну задачу и потом точно все 👍'
    await message.answer(text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
