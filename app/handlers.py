from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import  FSMContext

from app.service import kanye_quote
from app.database.requests import set_user
import app.Keyboards as kb
from app.Keyboards import phone_keyboard



router = Router()
class Reg(StatesGroup):
    name = State()
    number = State()
    anime = State()
    book = State()

    @router.message(CommandStart())
    async def cmd_start(message: Message, state: FSMContext):
        user_registered = await set_user(message.from_user.id)
        if user_registered:
            await message.answer(
                f"Привет, {message.from_user.first_name}! Давай начнем регистрацию.\nВведите ваше имя:")
            await state.set_state(Reg.name)
        else:
            await message.answer(
                f"Привет, {message.from_user.first_name}! Вы уже зарегистрированы.")  # Если пользователь уже есть


@router.callback_query(F.data=='quote')
async def callback_quote(call: CallbackQuery):
    quote = await kanye_quote()
    await call.message.answer(quote)
    await call.answer()



@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer("КОМАНДЫ: \n ПОВТОРНЯ РЕГИСТРАЦИЯ /reg\nПОМОЩЬ /help\nНАПИСАТЬ ТЕХ. ПОДЕРЖКА /support")


@router.message(F.text == "How are you?")
async  def how_are_you(message: Message):

    await message.answer("OK!")

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"id photo {message.photo[-1].file_id}")

@router.callback_query(F.data == 'catalog')
async def catalog(callback:CallbackQuery):
    await callback.answer('Вы выбрали каталог')
    await callback.message.edit_text("Каталог нашего магазина 🎯 ", reply_markup=await kb.inline_cloth())

@router.callback_query(F.data =='contacts')
async  def contacts(callback:CallbackQuery):
    await callback.answer("Вы выбрали Контакты")
    await callback.message.edit_text("Наши контакты:", reply_markup=await kb.inline_contacts())

@router.message

@router.message(Command("reg"))
async def reg_one(message: Message, state:FSMContext):
    await  state.set_state(Reg.name)
    await message.answer("Введите ваше имя:")

@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите номер:', reply_markup=phone_keyboard)

@router.message(Reg.anime)
async def reg_three(message: Message, state: FSMContext):
    await state.update_data(anime=message.text)
    await state.set_state(Reg.book)
    await message.answer("Какую книгу вы любите?")



@router.message(Reg.number)
async def two_three(message: Message, state: FSMContext):
    if message.contact:
        phone_number = message.contact.phone_number
    else:
        phone_number = message.text
    await state.update_data(number=phone_number)
    await state.set_state(Reg.anime)
    await message.answer("Ваше любимое аниме?")
@router.message(Reg.book)
async def reg_four(message: Message, state: FSMContext):
    await state.update_data(book=message.text)  # Сохраняем книгу
    data = await state.get_data()
    await message.answer(f"Cпасибо, регистрация прошла успешно!\nИмя: {data['name']}\nНомер: {data['number']}\nВаше любимое аниме: {data['anime']}\nЛюбимая книга: {data['book']}\n Теперь благодаря этому опросу, ваши рекомендации изменились", reply_markup=kb.main)
    await state.clear()


