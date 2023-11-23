from aiogram import Router, types
from aiogram.filters import Command


myinfo_router = Router()


@myinfo_router.message(Command('myinfo'))
async def myinfo(message: types.Message):
    user_info = (
        f"Ваш id: {message.from_user.id}\n"
        f"Имя: {message.from_user.first_name}\n"
        f"Username: @{message.from_user.username}"
    )
    await message.answer(user_info)