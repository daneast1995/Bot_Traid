import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold


TOKEN_API = '6883416515:AAH5yspjd9r7vP8kSaatOjmbSUGtkGs98wA'

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    try:
        #await message.send_copy(chat_id=message.chat.id)
        await message.answer(text=message.text)
    except Exception as err:
        print(err)

@dp.message()
async def command_handler(message: Message):
    try:
        #await message.send_copy(chat_id=message.chat.id)
        await message.answer(text=message.text)
    except Exception as err:
        print(err)
async def main():

    bot  = Bot(TOKEN_API)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())





