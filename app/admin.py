# Стандартные импорты
from aiogram import Bot, F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

# Импорт клавиатур
import app.keyboard as kb
from app.states import AdminStates

# Импорты функций db
from database.queries import get_user_id

# Инициализация админ роутера
admin_router = Router()


# Функция для отправки сообщения в топик
async def send_to_topic(bot: Bot, chat_id, thread_id, text):
    await bot.send_message(
        chat_id=chat_id,
        message_thread_id=thread_id,
        text=f"Новое сообщение:\n{text}",
    )
    await init_admin_menu(bot, chat_id, thread_id)


# Функция для отправки меню для админа в топике
async def init_admin_menu(bot: Bot, chat_id, thread_id):
    await bot.send_message(
        chat_id=chat_id,
        message_thread_id=thread_id,
        text="Выберите действие:",
        reply_markup=kb.new_topic,
    )


# Обработчик кнопки "Ответить" (callback: reply_admin)
@admin_router.callback_query(F.data == "reply_admin")
async def admin_reply_message(callback: CallbackQuery, state: FSMContext):
    callback.answer("Loading...")
    await state.set_state(AdminStates.reply)
    await callback.message.edit_text("Отправьте ответ:", reply_markup=kb.admin_cancel)


# Обработчик стейта "AdminStates.reply"
@admin_router.message(AdminStates.reply)
async def send_to_user(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(reply=message.text)
    await state.set_state(AdminStates.reply)

    # Получение сообщения админа
    admin_text = await state.get_data()
    admin_text = admin_text["reply"]

    # Получение user_id и отправка в переписку с юзером
    thread_id = message.message_thread_id
    user_id = await get_user_id(thread_id)
    await bot.send_message(chat_id=user_id, text=f"Ответ от админа:\n{admin_text}")


# Обработчик кнопки "Отмена" (callback: cancel)
@admin_router.callback_query(F.data == "admin_cancel")
async def admin_cancel(callback: CallbackQuery):
    await callback.message.edit_text(
        "Выберите действие:",
        reply_markup=kb.new_topic,
    )
