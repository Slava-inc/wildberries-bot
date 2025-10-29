from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import DATABASE_URL

# Создание асинхронного движка
engine = create_async_engine(DATABASE_URL)

# Создание фабрики сессий
async_session = async_sessionmaker(engine, expire_on_commit=False)