from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from config import TELEGRAM_BOT_TOKEN, REDIS_URL
from handlers import start, search
import asyncio

async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    storage = RedisStorage.from_url(REDIS_URL)
    dp = Dispatcher(storage=storage)

    dp.include_router(start.router)
    dp.include_router(search.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())