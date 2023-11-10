import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging
import random

BOT_TOKEN = '6321549390:AAEaMuJjFFLBaKYWXjlI27Frm1kHVNThTck'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Hi {message.from_user.first_name}")


@dp.message(Command('myinfo'))
async def myinfo(message: types.Message):
    user_info = (
        f"Ваш id: {message.from_user.id}\n"
        f"Имя: {message.from_user.first_name}\n"
        f"Username: @{message.from_user.username}"
    )
    await message.answer(user_info)


@dp.message(Command("pic"))
async def pic(message: types.Message):
    file = types.FSInputFile("images/dog.jpg")
    file2 = types.FSInputFile("images/eagle.jpg")
    file3 = types.FSInputFile("images/wolf.jpg")
    random_image = random.choice([file, file2, file3])

    await message.answer_photo(
        photo=random_image,
        caption="Собака, Орел, Волк"
    )



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
