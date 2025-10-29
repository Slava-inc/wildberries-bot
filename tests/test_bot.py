# tests/test_bot.py
import pytest
from unittest.mock import AsyncMock
from aiogram import Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.handlers.search import process_article
from bot.states import SearchStates

@pytest.mark.asyncio
async def test_process_article():
    message = AsyncMock(spec=Message)
    message.text = "123456789"
    state = FSMContext(storage=MemoryStorage(), key="test")

    await process_article(message, state)

    message.answer.assert_called()