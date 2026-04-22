# Базовые импорты
from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

# Импорт клавиатур
import app.keyboard as kb

# Импорт states
from app.states import UserReport

# Инициализация роутера
user_router = Router()


# Обработчик команды /start
@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=kb.start_keyboard)


# Обработчик кнопки "Помощь" (callback: help)
@user_router.callback_query(F.data == "help")
async def help_button(callback: CallbackQuery):
    await callback.answer("Loading...")
    await callback.message.edit_text("Функция в разработке")


# Обработчик кнопки "Новый тикет" (callback: new_ticket)
@user_router.callback_query(F.data == "new_ticket")
async def new_ticket(callback: CallbackQuery, state: FSMContext):
    await callback.answer("Loading...")
    await state.set_state(UserReport.report)
    await callback.message.edit_text("Пожалуйста, опишите вашу проблему:", reply_markup=kb.cancel)


# Обработчик стейта "UserReport.report"
@user_router.message(UserReport.report)
async def user_write(message: Message, state: FSMContext):
    await state.update_data(report=message.text)
    await state.set_state(UserReport.report)
    data = await state.get_data()
    print(data)
    await message.answer("Спасибо за ваш запрос!")
    await state.set_state(UserReport.waiting)


# Обработчик стейта "UserReport.waiting"
@user_router.message(UserReport.waiting)
async def cmd_wait(message: Message):
    await message.answer("Вы уже отправили свой запрос")


# Обработчик кнопки "Отмена" (callback: cancel)
@user_router.callback_query(F.data == "cancel")
async def cancel(callback: CallbackQuery):
    await callback.message.edit_text(
        "Добро пожаловать! Выберите действие:", reply_markup=kb.start_keyboard
    )
