# check_db.py
import asyncio
from db.session import async_session
from sqlalchemy import text

async def test_connection():
    async with async_session() as session:
        result = await session.execute(text("SELECT 1"))
        print("✅ Подключение к БД работает. Результат:", result.fetchone())

if __name__ == "__main__":
    asyncio.run(test_connection())