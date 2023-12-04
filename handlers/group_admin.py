from aiogram import Router, F, types
from aiogram.filters import Command
from pprint import pprint
group_messages_router = Router()
BAD_WORDS = ("дурак", "дура")


@group_messages_router.message(F.chat.type == "group")
@group_messages_router.message(Command("ban", prefix="!/"))
async def ban_user(message: types.Message):

    reply = message.reply_to_message
    if reply is not None:
        await message.bot.ban_chat_member(
            chat_id=message.chat.id,
            user_id=reply.from_user.id
        )
        await message.answer(f"Пользователь {message.from_user.username} забанен")


@group_messages_router.message(F.chat.type == "group")
@group_messages_router.message(Command("pin", prefix="!/"))
async def pin_message(message: types.Message):
    reply = message.reply_to_message
    if reply is not None:
        await message.bot.pin_chat_message(
            chat_id=message.chat.id,
            message_id=reply.message_id
        )


@group_messages_router.message(F.chat.type == "group")
async def catch_bad_words(message: types.Message):
    for word in BAD_WORDS:
        if word in message.text.lower():
            await message.reply(f"Нельзя использовать слово {word}!")
            await message.delete()
            break