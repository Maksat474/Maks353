from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            {
                types.InlineKeyboardButton(
                    text="Наш сайт", url="http://books.kg/"
                )
            },
            [
                types.InlineKeyboardButton(
                    text="Адрес", callback_data="address"
                ),
                types.InlineKeyboardButton(
                    text="Контакты", callback_data="contacts"
                ),
                types.InlineKeyboardButton(
                    text="О нас", callback_data="about"
                )
            ]
        ]
    )
    await message.answer(
        f"Hi @{message.from_user.username}, тебя зовут:{message.from_user.first_name}",
        reply_markup=kb
    )


@start_router.callback_query(F.data == "address")
async def address(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("ГУМ “Чынар”, 4 этаж")


@start_router.callback_query(F.data == "contacts")
async def contacts(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("0 (312) 88-24-45 ")


@start_router.callback_query(F.data == "about")
async def about_us(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Фирма «Раритет» была основана в марте 1992 года. В настоящее время это динамично "
                                  "развивающееся книготорговое и издательское предприятие. Книжные магазины фирмы "
                                  "находятся в центральной части столицы Кыргызстана – городе Бишкек.")

