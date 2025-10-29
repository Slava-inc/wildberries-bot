from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔍 Найти товар")],
        [KeyboardButton(text="📊 Статистика")],
    ],
    resize_keyboard=True
)