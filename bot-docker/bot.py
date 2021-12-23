import logging
import requests
from tok import tok

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = tok

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands = ['api'])
async def getapi(message: types.Message):
    ans = requests.get('http://172.17.0.2/home')
    await message.answer(ans.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)