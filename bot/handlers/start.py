# bot/handlers/start.py

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from bot.keyboards.main_menu import main_menu  # предполагается, что вы создали этот модуль
from db.session import async_session
from db.models import User
from sqlalchemy import select, insert

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    # Получаем ID пользователя Telegram
    tg_id = message.from_user.id

    # Проверяем, есть ли пользователь в базе
    async with async_session() as session:
        result = await session.execute(select(User).where(User.tg_id == tg_id))
        user = result.scalar_one_or_none()

        # Если пользователя нет, создаём нового
        if not user:
            new_user = User(tg_id=tg_id)
            session.add(new_user)
            await session.commit()

    # Отправляем приветственное сообщение
    await message.answer(
        "Привет! Я бот для поиска товаров на Wildberries.\n"
        "Нажмите кнопку ниже, чтобы начать поиск.",
        reply_markup=main_menu
    )