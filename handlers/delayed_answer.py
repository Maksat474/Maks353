from datetime import datetime
from aiogram import types, Router
from aiogram.filters import Command

from bot import scheduler, bot
from db.queries import get_all_subscribers


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
        send_reminder(),
        "date",
        run_date=datetime(2024, 1, 1, 0, 0, 0),
        kwargs={"chat_id": message.from_user.id}
    )
    await message.answer("Напоминание установлено")


async def send_reminder(chat_id: int):
    subscribers = get_all_subscribers(chat_id)
    for subscriber in subscribers:
        chat_id = subscriber['chat_id']
        await bot.send_message(chat_id=chat_id, text="С новым годом!")