# Базовые импорты
import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

# Импорт из файлов проекта
from app.admin import admin_router
from app.user import user_router
from database.init import init_db


async def main():
    # Основная функция бота
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.startup.register(start_app)
    dp.shutdown.register(shutdown)
    dp.include_routers(user_router, admin_router)
    await dp.start_polling(bot)


# startup функция
async def start_app(dispatcher: Dispatcher):
    await init_db()


# shutdown функция
async def shutdown(dispatcher: Dispatcher):
    print("Shutting down...")


# Старт бота
if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
