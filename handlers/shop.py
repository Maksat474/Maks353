from aiogram import F, Router, types
from aiogram.filters import Command
from bot import bot
from db import queries

shop_router = Router()


@shop_router.message(Command("shop"))
async def shop(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Книги")
            ],
            [
                types.KeyboardButton(text="Комиксы"),
                types.KeyboardButton(text="Сувениры"),
            ]
        ],
        resize_keyboard=True
    )

    await message.answer("Выберите категорию товаров:",
                         reply_markup=kb)


@shop_router.message(F.text == "Книги")
async def show_books(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    products = queries.get_product_by_category_id(1)
    for product in products:
        file = types.FSInputFile(product[3])
        await bot.send_photo(chat_id=message.from_user.id, photo=file, caption=f"name: {product[1]}\n"
                                                                               f"price: {product[2]}",
                             reply_markup=kb)


@shop_router.message(F.text == "Комиксы")
async def show_comics(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    products = queries.get_product_by_category_id(2)
    for product in products:
        file = types.FSInputFile(product[3])
        await bot.send_photo(chat_id=message.from_user.id, photo=file, caption=f"name: {product[1]}\n"
                                                                               f"price: {product[2]}",
                             reply_markup=kb)


@shop_router.message(F.text == "Сувениры")
async def show_comics(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    products = queries.get_product_by_category_id(3)
    for product in products:
        file = types.FSInputFile(product[3])
        await bot.send_photo(chat_id=message.from_user.id, photo=file, caption=f"name: {product[1]}\n"
                                                                               f"price: {product[2]}",
                             reply_markup=kb)