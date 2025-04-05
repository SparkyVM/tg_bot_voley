import asyncio
from create_bot import bot, dp, admins
from data_base.base import create_tables
from aiogram.types import BotCommand, BotCommandScopeDefault
from handlers.start_router import start_router
from handlers.location.show_location_router import show_loc_router
from handlers.news.show_news_router import show_news_router
from handlers.about.show_info import show_info_router
from handlers.reserve.show_reserves_router import show_reserves_router


async def set_commands():
    """Функция настройки командного меню. Дефолтное для всех пользователей"""
    commands = [BotCommand(command='start', description='Старт')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def start_bot():
    """Функция, которая выполнится когда бот запустится"""
    await set_commands()
    await create_tables()
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, 'Бот запущен 🥳')
        except:
            pass


async def stop_bot():
    """Функция, которая выполнится когда бот завершит свою работу"""
    try:
        for admin_id in admins:
            await bot.send_message(admin_id, 'Бот остановлен 😔')
    except:
        pass


async def main():
    # регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(show_loc_router)
    dp.include_router(show_news_router)
    dp.include_router(show_info_router)
    dp.include_router(show_reserves_router)

    # регистрация функций
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    # запуск бота в режиме long polling при запуске бот очищает все обновления, которые были за его моменты бездействия
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())