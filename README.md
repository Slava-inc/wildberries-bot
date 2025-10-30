# Telegram-бот для интеграции с Wildberries

Этот бот позволяет пользователям получать информацию о товарах на маркетплейсе Wildberries: остатки, цены, скидки и другую аналитику. Проект разработан с использованием Python, aiogram, SQLAlchemy, PostgreSQL, Redis и Docker.

## 🧱 Архитектура

- **Telegram-бот**: `aiogram` (асинхронный фреймворк)
- **API**: `aiohttp` для запросов к Wildberries
- **База данных**: `PostgreSQL` с `asyncpg` (асинхронный драйвер)
- **Кеширование**: `Redis`
- **Мокирование**: `FastAPI` для эмуляции API Wildberries
- **Контейнеризация**: `Docker` + `docker-compose`

## 📋 Функционал

- Регистрация пользователей
- Поиск товара по артикулу
- Отображение цены, остатков, скидок
- Подписка на уведомления об изменении цены/остатка
- Хранение истории запросов

## 🚀 Установка и запуск

### 1. Подготовка

#### 1. Убедитесь, что у вас установлены:
   - [Docker](https://www.docker.com/products/docker-desktop/)
   - [Docker Compose](https://docs.docker.com/compose/install/)

#### 2. Склонируйте репозиторий:

   - git clone https://github.com/your-username/wildberries_bot.git
   - cd wildberries_bot
#### 3. Создайте файл env_var в корне проекта:

   - TELEGRAM_BOT_TOKEN=your_bot_token
   - DATABASE_URL=postgresql+asyncpg://user:password@db:5432/wildberries_bot
   - REDIS_URL=redis://redis:6379
   - WB_API_URL=http://mock:8000/api

#### 4. Запуск с помощью Docker Compose
   - docker compose up --build
     
⚠️ Флаг --build пересобирает образы, если вы вносили изменения в Dockerfile. 

#### 5. Выполнение миграций
Если вы хотите выполнить миграции вручную (или до запуска бота):

Убедитесь, что БД запущена:

   - docker compose up -d db

Выполните миграции:

##### Для Linux/Mac
   - cat migrations/001_create_users_table.sql | docker exec -i wildberries_bot-db-1 psql -U user -d wildberries_bot
   - cat migrations/002_add_subscriptions_table.sql | docker exec -i wildberries_bot-db-1 psql -U user -d wildberries_bot

##### Для Windows PowerShell
   - Get-Content migrations/001_create_users_table.sql | docker exec -i wildberries_bot-db-1 psql -U user -d wildberries_bot
   - Get-Content migrations/002_add_subscriptions_table.sql | docker exec -i wildberries_bot-db-1 psql -U user -d wildberries_bot
### 2. 🧪 Тестирование и отладка
Проверка подключения к БД извне (локально)

Пробросить порт PostgreSQL на хост. Добавьте в `docker-compose.yml` для сервиса `db`:

```yaml
services:
  db:
    image: postgres:15
    ports:
      - "5432:5432"  # <-- Добавьте эту строку
    environment:
      POSTGRES_DB: wildberries_bot
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_/var/lib/postgresql/data
```
Изменить DATABASE_URL в env_var на localhost:

DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/wildberries_bot

Активируйте виртуальное окружение (если ещё не активировано):

```
python -m venv .env
source env_var/bin/activate  # Linux/Mac
env_var\Scripts\activate     # Windows
pip install -r requirements.txt
```
Создайте тестовый скрипт check_db.py:

``` check_db.py
import asyncio
from sqlalchemy import text
from db.session import async_session

async def test_connection():
    async with async_session() as session:
        result = await session.execute(text("SELECT 1"))
        print("✅ Подключение к БД работает. Результат:", result.fetchone())

if __name__ == "__main__":
    asyncio.run(test_connection())
```
Запустите скрипт:

python check_db.py

Ожидаемый результат:
```
✅ Подключение к БД работает. Результат: (1,)
❌ Если вы получаете ошибку socket.gaierror: [Errno 11001] getaddrinfo failed,
это означает, что имя хоста (например, db) не может быть разрешено. 
Убедитесь, что вы используете localhost, если запускаете скрипт локально, а не внутри Docker-контейнера.
Также проверьте, что порт 5432 проброшен на хост и PostgreSQL в контейнере запущен и слушает этот порт. 
Эта ошибка часто возникает, если вы пытаетесь подключиться к БД с хоста, но DATABASE_URL всё ещё указывает на имя сервиса db, доступное только внутри Docker-сети. 
Измените его на localhost, как описано выше, и убедитесь, что контейнер БД запущен и порт проброшен. 
```

Запуск мок-сервера отдельно

Мок-сервер API Wildberries можно запустить отдельно:

docker build -f Dockerfile.mock -t mock-wb .
docker run -d -p 8001:8000 --name mock mock-wb
Тогда замените WB_API_URL в env_var на:

WB_API_URL=http://localhost:8001/api

### 📁 Структура проекта
```
wildberries_bot/
├── bot/                    # Код бота (aiogram)
│   ├── handlers/
│   ├── keyboards/
│   ├── states.py
│   └── main.py
├── api/                    # API для Wildberries (реальное и мок)
├── db/                     # Модели и сессия SQLAlchemy
├── cache/                  # Клиент Redis
├── migrations/             # SQL-скрипты миграций
├── config.py               # Настройки
├── env_var                    # Переменные окружения
├── docker-compose.yml
├── Dockerfile
├── Dockerfile.mock
├── requirements.txt
└── README.md
```
### 🛠️ Технологии

- Python 3.11
- aiogram 3.x
- SQLAlchemy 2.x (async)
- PostgreSQL
- Redis
- Docker
- FastAPI (для мок-сервера)

### 📝 Лицензия
MIT
