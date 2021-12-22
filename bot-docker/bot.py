import logging
import requests

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '2122770904:AAHBJKDxJnaQDTkbGHyMdZME78eLhN7xtYc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

@dp.message_handler(commands = ['api'])
async def getapi(message: types.Message):
    ans = requests.get('http://172.17.0.2/home')
    print(ans)
    await message.answer(ans)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)