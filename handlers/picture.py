from aiogram import Router, types
from aiogram.filters import Command
import random
from pathlib import Path


picture_router = Router()

@picture_router.message(Command("pic"))
async def pic(message: types.Message):
    image_directory = Path("images")
    image_files = list(image_directory.iterdir())
    random_image = random.choice(image_files)
    file = types.FSInputFile(random_image)


    await message.answer_photo(
        photo=file
    )