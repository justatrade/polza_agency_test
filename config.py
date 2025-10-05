"""
Конфигурация бота.
"""

import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env
load_dotenv()

# Токен Telegram-бота
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Проверка наличия токена
if not BOT_TOKEN:
    raise ValueError("Не указан BOT_TOKEN в переменных окружения!")
