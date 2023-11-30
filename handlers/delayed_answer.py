from datetime import datetime
from aiogram import types, Router
from aiogram.filters import Command

from bot import scheduler, bot


delayed_answer_router = Router()


@delayed_answer_router.message(Command("remind"))
async def remind(message: types.Message):
    # scheduler.add_job(
    #     send_remider,
    #     "interval",
    #     seconds=5,
    #     kwargs={"chat_id": message.from_user.id},
    # )
    scheduler.add_job(
        send_remider,
        "date",
        run_date=datetime(2024, 1, 1, 0, 0, 0),
        kwargs={"chat_id": message.from_user.id}
    )
    await message.answer("Напоминание установлено")


async def send_remider(chat_id: int):
    await bot.send_message(chat_id=chat_id, text="Напоминалка")