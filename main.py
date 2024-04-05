import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
import logging
from handlers import common, registration, news


async def main():
    # Включаем логгирование
    logging.basicConfig(level=logging.INFO)

    # Создаем объект бота
    bot = Bot(token=config.token)

    # Диспечер
    dp = Dispatcher()

    dp.include_router(registration.router)        # Подключаем Роутер на обработку Записи
    dp.include_router(news.router)          # Подключаем Роутер на обработку Новостей
    dp.include_router(common.router)        # Подключаем Роутер на обработку сообщений

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())