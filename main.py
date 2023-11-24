from aiogram.types import BotCommand
import asyncio
import logging
from bot import dp, bot
from handlers import (
    start_router,
    myinfo_router,
    picture_router,
    echo_router,
    shop_router,
    questions_router
)


async def main():
    await bot.set_my_commands([
        BotCommand(command="start", description="начало"),
        BotCommand(command="myinfo", description="информация обо мне"),
        BotCommand(command="pic", description="показать картинку"),
        BotCommand(command="shop", description="магазин"),
        BotCommand(command="quest", description="опросник"),
        BotCommand(command="echo", description="эхо")
    ])
    dp.include_router(start_router)
    dp.include_router(myinfo_router)
    dp.include_router(picture_router)
    dp.include_router(shop_router)
    dp.include_router(questions_router)
    dp.include_router(echo_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())