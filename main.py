# Базовые импорты
import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

# Импорт из файлов проекта
from app.admin import admin_router
from app.user import user_router
from database.init import init_db

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


async def main():
    # Основная функция бота
    bot = Bot(token=os.getenv("TOKEN"))
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.startup.register(start_app)
    dp.shutdown.register(shutdown)
    dp["dp"] = dp
    dp.include_routers(user_router, admin_router)

    logger.info("Бот запускается...")
    await dp.start_polling(bot)


# startup функция
async def start_app(dispatcher: Dispatcher):
    await init_db()
    logger.info("База данных инициализирована")


# shutdown функция
async def shutdown(dispatcher: Dispatcher):
    logger.info("Бот останавливается")


# Старт бота
if __name__ == "__main__":
    load_dotenv()
    asyncio.run(main())
