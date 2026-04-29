# Основные импорты
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Клавиатура для главного меню
start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Новый тикет", callback_data="new_ticket")],
        [InlineKeyboardButton(text="Помощь", callback_data="help")],
    ]
)

# Клавиатура для отмены действия
cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Отмена", callback_data="cancel")],
    ]
)

# Клавиатура для отмены действия админа
admin_cancel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Отмена", callback_data="admin_cancel")],
    ]
)


# Клавиатура для нового топика в админ-группе
new_topic = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ответить", callback_data="reply_admin")],
        [InlineKeyboardButton(text="Закрыть тикет", callback_data="close_ticket")],
    ]
)
