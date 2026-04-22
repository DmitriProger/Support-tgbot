# Основные импорты
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Клавиатура для главного меню
start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="Новый тикет", callback_data="new_ticket")]]
)

# Клавиатура для отмены действия
cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Отмена", callback_data="cancel")],
    ]
)
