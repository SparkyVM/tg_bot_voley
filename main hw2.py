import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
import logging
from handlers import common, flower


async def main():
    # Включаем логгирование
    logging.basicConfig(level=logging.INFO)

    # Создаем объект бота
    bot = Bot(token=config.token)

    # Диспечер
    dp = Dispatcher()

    dp.include_router(flower.router)        # Подключаем Роутер на обработку Цветы
    dp.include_router(common.router)        # Подключаем Роутер на обработку сообщений

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())