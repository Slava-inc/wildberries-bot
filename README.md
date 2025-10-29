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

1. Убедитесь, что у вас установлены:
   - [Docker](https://www.docker.com/products/docker-desktop/)
   - [Docker Compose](https://docs.docker.com/compose/install/)

2. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/your-username/wildberries_bot.git
   cd wildberries_bot
PostgreSQL
Redis
Docker
FastAPI (для мок-сервера)
📝 Лицензия
