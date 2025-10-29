import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='env_var')

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")
WB_API_URL = os.getenv("WB_API_URL")