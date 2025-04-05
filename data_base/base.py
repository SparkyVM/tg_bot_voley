from .database import async_session, engine, Base


def connection(func):
    """Функция для взаимодействия с подключением"""
    async def wrapper(*args, **kwargs):
        async with async_session() as session:
            return await func(session, *args, **kwargs)

    return wrapper


async def create_tables():
    """Функция для создания таблиц БД"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)