from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from bot.keyboards.main_menu import main_menu
from bot.states import SearchStates
from api.wildberries import get_product_info
from db.models import User
from db.session import async_session
from sqlalchemy import select

router = Router()

@router.message(F.text == "🔍 Найти товар")
async def cmd_search(message: Message, state: FSMContext):
    await message.answer("Введите артикул товара:", reply_markup=None)
    await state.set_state(SearchStates.waiting_for_article)

@router.message(SearchStates.waiting_for_article)
async def process_article(message: Message, state: FSMContext):
    article = message.text
    if not article.isdigit():
        await message.answer("Артикул должен быть числом.")
        return

    data = await get_product_info(article)
    if data:
        product = data['data']['products'][0]
        await message.answer(f"Название: {product['name']}\nЦена: {product['price']}\nОстаток: {product['stock']}", reply_markup=main_menu)
    else:
        await message.answer("Товар не найден.", reply_markup=main_menu)

    await state.clear()