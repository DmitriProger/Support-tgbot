import aiosqlite

DB_PATH = "app.db"


# Создание таблиц
async def init_db():
    async with aiosqlite.connect(DB_PATH) as conn:
        await conn.execute("""CREATE TABLE IF NOT EXISTS user_topic (
                user_id INTEGER PRIMARY KEY,
                thread_id INTEGER NOT NULL 
            )                  
        """)
        await conn.commit()
