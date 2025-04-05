from create_bot import logger
from .base import connection
from .models import User, News, Info, Location, Court, Reserve
from sqlalchemy import select
from typing import List, Dict, Any, Optional
from sqlalchemy.exc import SQLAlchemyError


@connection
async def set_user(session, tg_id: int, username: str, full_name: str) -> Optional[User]:
    """Функция получения Пользователя"""
    try:
        user = await session.scalar(select(User).filter_by(id=tg_id,))

        if not user:
            new_user = User(id=tg_id, username=username, full_name=full_name)
            session.add(new_user)
            await session.commit()
            logger.info(f"Зарегистрировал пользователя с ID {tg_id}!")
            return None
        else:
            logger.info(f"Пользователь с ID {tg_id} найден!")
            return user
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при добавлении пользователя: {e}")
        await session.rollback()

@connection
async def get_locations(session) -> List[Dict[str, Any]]:
    """Функция для получения Местоположений"""
    try:
        result = await session.execute(select(Location))
        locations = result.scalars().all()

        loc_list = [
            {
                #'id': loc.id,
                'name': loc.name,
                'adress': loc.adress,
                'phone_number': loc.phone_number,
                #'courts': loc.courts
            } for loc in locations
        ]
        return loc_list
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при получении Местоположений: {e}")
        return []

@connection
async def get_courts(session, loc_name: str) -> List[Dict[str, Any]]:
    """Функция для получения Кортов"""
    try:
        location_req = await session.execute(select(Location).filter_by(name=loc_name,))
        location = location_req.scalars().first()
        courts_req = await session.execute(select(Court).filter_by(location_id=location.id,))
        courts = courts_req.scalars().all()

        court_list = [
            {
                'court_name': court.court_name,
            } for court in courts
        ]
        return court_list
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при получении Кортов: {e}")
        return []

@connection
async def get_news(session) -> List[Dict[str, Any]]:
    """Функция для получения списка опубликованных Новостей"""
    try:
        result = await session.execute(select(News).where(News.is_published==True))
        news = result.scalars().all()

        post_list = [
            {
                'id': post.id,
                'title': post.title,
                'content': post.content
            } for post in news
        ]
        return post_list
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при получении Новостей: {e}")
        return []

@connection
async def get_post(session, post_title: str) -> List[Dict[str, Any]]:
    """Функция для получения выбранной Статьи"""
    try:
        result = await session.execute(select(News).filter_by(title=post_title))
        news = result.scalars().all()

        if not news:
            logger.info(f"Новость не найдена.")
            return []

        post_list = [
            {
                'id': post.id,
                'title': post.title,
                'content': post.content
            } for post in news
        ]

        return post_list
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при получении Новости: {e}")
        return []


@connection
async def get_about(session) -> str:
    """Функция для получения информации о Компании"""
    try:
        result = await session.execute(select(Info).filter_by(name='about'))
        info_about = result.scalars().first()
        if not info_about:
            logger.info("Информация отсутствует.")
            return "Информация отсутствует."
        return info_about.text
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при получении информации: {e}")
        return 'Ошибка'


@connection
async def get_reserves_by_user(session, user_id: int, date_add: str = None, text_search: str = None,
                            content_type: str = None) -> List[Dict[str, Any]]:
    try:
        result = await session.execute(select(Reserve).filter_by(user_id=user_id))
        reserves = result.scalars().all()

        if not reserves:
            logger.info(f"Брони пользователя с ID {user_id} не найдены.")
            return []

        reserves_list = [
            {
                'id': reserve.id,
                'date_reserve': reserve.date_reserve,
                'time_reserve': reserve.time_reserve,
                'court_id': reserve.court_id
            } for reserve in reserves
        ]

        return reserves_list

    except SQLAlchemyError as e:
        logger.error(f"Ошибка при получении броней: {e}")
        return []


'''
@connection
async def add_note(session, user_id: int, content_type: str,
                   content_text: Optional[str] = None, file_id: Optional[str] = None) -> Optional[Note]:
    try:
        user = await session.scalar(select(User).filter_by(id=user_id))
        if not user:
            logger.error(f"Пользователь с ID {user_id} не найден.")
            return None

        new_note = Note(
            user_id=user_id,
            content_type=content_type,
            content_text=content_text,
            file_id=file_id
        )

        session.add(new_note)
        await session.commit()
        logger.info(f"Заметка для пользователя с ID {user_id} успешно добавлена!")
        return new_note
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при добавлении заметки: {e}")
        await session.rollback()


@connection
async def update_text_note(session, note_id: int, content_text: str) -> Optional[Note]:
    try:
        note = await session.scalar(select(Note).filter_by(id=note_id))
        if not note:
            logger.error(f"Заметка с ID {note_id} не найдена.")
            return None

        note.content_text = content_text
        await session.commit()
        logger.info(f"Заметка с ID {note_id} успешно обновлена!")
        return note
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при обновлении заметки: {e}")
        await session.rollback()


@connection
async def get_notes_by_userc

        note_list = [
            {
                'id': note.id,
                'content_type': note.content_type,
                'content_text': note.content_text,
                'file_id': note.file_id,
                'date_created': note.created_at
            } for note in notes
        ]

        if date_add:
            note_list = [note for note in note_list if note['date_created'].strftime('%Y-%m-%d') == date_add]

        if text_search:
            note_list = [note for note in note_list if text_search.lower() in (note['content_text'] or '').lower()]

        if content_type:
            note_list = [note for note in note_list if note['content_type'] == content_type]

        return note_list
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при получении заметок: {e}")
        return []


@connection
async def get_note_by_id(session, note_id: int) -> Optional[Dict[str, Any]]:
    try:
        note = await session.get(Note, note_id)
        if not note:
            logger.info(f"Заметка с ID {note_id} не найдена.")
            return None

        return {
            'id': note.id,
            'content_type': note.content_type,
            'content_text': note.content_text,
            'file_id': note.file_id
        }
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при получении заметки: {e}")
        return None


@connection
async def delete_note_by_id(session, note_id: int) -> Optional[Note]:
    try:
        note = await session.get(Note, note_id)
        if not note:
            logger.error(f"Заметка с ID {note_id} не найдена.")
            return None

        await session.delete(note)
        await session.commit()
        logger.info(f"Заметка с ID {note_id} успешно удалена.")
        return note
    except SQLAlchemyError as e:
        logger.error(f"Ошибка при удалении заметки: {e}")
        await session.rollback()
        return None
'''