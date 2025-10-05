# Telegram Bot - Polza Agency Test

## Описание

Это тестовый Telegram-бот, созданный для демонстрации базовой структуры проекта с использованием python-telegram-bot.

## Структура проекта

```
.
├── bot.py              # Главный файл запуска бота
├── config.py           # Конфигурация и переменные окружения
├── handlers.py         # Обработчики команд и сообщений
├── requirements.txt    # Зависимости проекта
├── .env.example        # Пример файла переменных окружения
└── README.md           # Документация
```

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/justatrade/polza_agency_test.git
cd polza_agency_test
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл `.env` на основе `.env.example`:
```bash
cp .env.example .env
```

4. Добавьте ваш токен Telegram бота в файл `.env`:
```
BOT_TOKEN=ваш_токен
```

## Запуск

```bash
python bot.py
```

## Доступные команды

- `/start` - Начать работу с ботом
- `/help` - Показать список доступных команд

## Технологии

- Python 3.8+
- python-telegram-bot 20.7
- python-dotenv

## Лицензия

MIT
