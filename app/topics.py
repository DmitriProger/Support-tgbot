# Базовые импорты
from aiogram import Bot

# Импорты из других файлов
from database.queries import get_topic, save_topic


# Функция создания топика и вызов save_topic для сохранения в db
async def create_topic(bot: Bot, chat_id, user_id, name):
    topic = await bot.create_forum_topic(chat_id=chat_id, name=name)
    await save_topic(user_id, topic.message_thread_id)
    return topic.message_thread_id


# Функция для отправки сообщения в топик
async def send_to_topic(bot: Bot, chat_id, thread_id, text):
    await bot.send_message(
        chat_id=chat_id,
        message_thread_id=thread_id,
        text=text,
    )


# Функция для получения id топика
async def get_or_create_topic(bot: Bot, chat_id, user_id, name):
    thread_id = await get_topic(user_id)
    print(f"get_topic вернул: {thread_id}")

    if thread_id is None:
        thread_id = await create_topic(bot, chat_id, user_id, f"юзер: {name}")
        print(f"создан топик: {thread_id}")

    return thread_id
