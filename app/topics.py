# Базовые импорты
import logging

from aiogram import Bot

# Импорты из других файлов
from database.queries import get_topic, save_topic

logger = logging.getLogger(__name__)


# Функция создания топика и вызов save_topic для сохранения в db
async def create_topic(bot: Bot, chat_id, user_id, name):
    topic = await bot.create_forum_topic(chat_id=chat_id, name=name)
    await save_topic(user_id, topic.message_thread_id)
    logger.info("Создан топик thread_id=%s для user_id=%s", topic.message_thread_id, user_id)
    return topic.message_thread_id


# Функция для получения id топика
async def get_or_create_topic(bot: Bot, chat_id, user_id, name):
    thread_id = await get_topic(user_id)
    logger.debug("get_topic для user_id=%s вернул thread_id=%s", user_id, thread_id)

    if thread_id is None:
        thread_id = await create_topic(bot, chat_id, user_id, f"юзер: {name}")

    return thread_id
