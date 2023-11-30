from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from db.queries import save_questionaire

questions_router = Router()


class Questionaire(StatesGroup):
    name = State()
    age = State()
    gender = State()
    occupation = State()
    education = State()
    favorite_genre_of_literature = State()
    favorite_autor = State()
    favorite_piece = State()


# FSM - Finite state machine(Конечный автомат)
@questions_router.message(Command("stop"))
@questions_router.message(F.text == "stop")
async def stop_questions(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Вопросы прерваны")


@questions_router.message(Command("quest"))
async def start_questions(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.name)
    await message.answer("Для выхода введите 'stop")
    await message.answer("Как вас зовут?")


@questions_router.message(F.text, Questionaire.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Questionaire.age)
    await message.answer("Какой у вас возраст?")


@questions_router.message(F.text, Questionaire.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Возраст должен быть числом!")
    elif int(age) < 12 or int(age) > 100:
        await message.answer("Возраст должен быть от 12 до 100")
    else:
        await state.update_data(age=int(age))

        kb = types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(text="Мужской"),
                    types.KeyboardButton(text="Женский")
                ]
            ]
        )
        await state.set_state(Questionaire.gender)
        await message.answer("Ваш пол?",
                             reply_markup=kb)


@questions_router.message(F.text, Questionaire.gender)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)
    await state.set_state(Questionaire.occupation)
    await message.answer("ваш род деятельности?")


@questions_router.message(F.text, Questionaire.occupation)
async def process_occupation(message: types.Message, state: FSMContext):
    await state.update_data(oсcupation=message.text)
    await state.set_state(Questionaire.education)
    await message.answer("ваше образование?")


@questions_router.message(F.text, Questionaire.education)
async def process_education(message: types.Message, state: FSMContext):
    await state.update_data(education=message.text)
    await state.set_state(Questionaire.favorite_genre_of_literature)
    await message.answer("Ваш любимый жанр литературы?")


@questions_router.message(F.text, Questionaire.favorite_genre_of_literature)
async def process_favorite_genre_of_literature(message: types.Message, state: FSMContext):
    await state.update_data(favorite_genre_of_literature=message.text)
    await state.set_state(Questionaire.favorite_autor)
    await message.answer("Ваш любимый автор?")


@questions_router.message(F.text, Questionaire.favorite_autor)
async def process_favorite_autor(message: types.Message, state: FSMContext):
    await state.update_data(favorite_autor=message.text)
    await state.set_state(Questionaire.favorite_piece)
    await message.answer("Ваше любимое произведение?")


@questions_router.message(F.text, Questionaire.favorite_piece)
async def process_favorite_piece(message: types.Message, state: FSMContext):
    await state.update_data(favorite_piece=message.text)

    # save to DB
    data = await state.get_data()
    save_questionaire(data)
    # print(data)
    # clear state
    await state.clear()
    await message.answer("Спасибо, что прошли опросник!")