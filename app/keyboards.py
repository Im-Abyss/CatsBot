from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram.utils.keyboard import InlineKeyboardBuilder

add_cats = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Фото котиков 🐱")],
    ],
    resize_keyboard=True
)