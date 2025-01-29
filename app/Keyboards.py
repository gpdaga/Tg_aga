from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог 🌟 ', callback_data='catalog')],
    [InlineKeyboardButton(text="Корзина 🔎 ", callback_data='basket')],
    [InlineKeyboardButton(text="Контакты 🔧 ", callback_data='contacts')]
])


settings1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Перейти на YouTube', url='https://youtu.be/qRyshRUA0xM')]
])

cloths = ["🧥 Куртки", "🧢 Шапки", "👖 Штаны", "👕 Футболки"]
basket = []
contacts = ['+997 700 100 100','+996 909 999']

async def inline_cloth():
    keyboard = InlineKeyboardBuilder()
    for cloth in cloths:
        keyboard.add(InlineKeyboardButton(text=cloth, url="https://www.google.kg/?hl=ru"))
    return keyboard.adjust(2).as_markup()

async def inline_contacts():
    keyboard = InlineKeyboardBuilder()
    for contact in contacts:
        keyboard.add(InlineKeyboardButton(text=contact, url="https://www.whatsapp.com/?lang=ru_RU"))
    return keyboard.adjust(2).as_markup()

phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📱 Отправить номер", request_contact=True)]],
    resize_keyboard=True,
    one_time_keyboard=True
)