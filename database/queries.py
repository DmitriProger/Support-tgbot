import aiosqlite

from database.init import DB_PATH


# Сохранение информации о новом топике в db
async def save_topic(user_id, thread_id):
    async with aiosqlite.connect(DB_PATH) as conn:
        await conn.execute(
            "INSERT INTO user_topic(user_id, thread_id) VALUES (?, ?)",
            (user_id, thread_id),
        )

        await conn.commit()


# Получение id топика
async def get_topic(user_id):
    async with aiosqlite.connect(DB_PATH) as conn:
        cursor = await conn.execute(
            "SELECT thread_id FROM user_topic WHERE user_id = ?", (user_id,)
        )
        row = await cursor.fetchone()
        return row[0] if row else None


# Получение id юзера
async def get_user_id(thread_id):
    async with aiosqlite.connect(DB_PATH) as conn:
        cursor = await conn.execute(
            "SELECT user_id FROM user_topic WHERE thread_id = ?", (thread_id,)
        )
        row = await cursor.fetchone()
        return row[0]
