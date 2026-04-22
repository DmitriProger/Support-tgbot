# Стандартные импорты
from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

# Импорт клавиатур
import app.keyboard as kb

# Инициализация админ роутера
admin_router = Router()


# Обработчик команды /start
@admin_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("тест")
