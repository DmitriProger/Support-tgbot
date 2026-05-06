# Базовые импорты
import asyncio
import os

from aiogram import Bot, F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

# Импорт клавиатур
import app.keyboard as kb

# Импорт states
from app.states import UserReport

# Импорт из других файлов
from app.topics import get_or_create_topic
from app.admin import send_to_topic

# Инициализация роутера
user_router = Router()


# Обработчик команды start
@user_router.message(CommandStart())
async def new_ticket(message: Message, state: FSMContext):
    await state.set_state(UserReport.report)
    await message.answer("Здравствуйте, напишите текст вашего обращения")


# Обработчик стейта "UserReport.report"
@user_router.message(UserReport.report)
async def user_write(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(report=message.text)
    await state.set_state(UserReport.report)

    # Получение текста юзера
    user_text = await state.get_data()
    user_text = user_text["report"]

    # Получение id топика
    group_id = int(os.getenv("GROUP_ID"))
    thread_id = await get_or_create_topic(
        bot, group_id, message.from_user.id, message.from_user.full_name
    )

    # Отправка сообщения в топик
    await send_to_topic(bot, group_id, thread_id, user_text)

    await state.set_state(UserReport.waiting)


# Обработчик стейта "UserReport.waiting"
@user_router.message(UserReport.waiting)
async def cmd_wait(message: Message):
    await message.answer("Вы уже отправили свой запрос")
