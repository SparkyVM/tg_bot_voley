from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from create_bot import bot
from data_base.dao import get_news, get_post
from keyboards.reply_menu_kb import main_kb, news1_kb
from keyboards.gen_other_kb import generate_news_kb
from utils.utils import send_post

show_news_router = Router()


class FindNoteStates(StatesGroup):
    text = State()  # Ожидаем любое сообщение от пользователя


@show_news_router.message(F.text == '/новости')
async def show_all_news(message: Message, state: FSMContext):
    """Функция для получения всех Новостей"""
    await state.clear()
    all_news = await get_news()
    if all_news:
        await message.answer('Новости:', reply_markup=generate_news_kb(all_news))
    else:
        await message.answer('Нет информации для отображения!', reply_markup=main_kb())


@show_news_router.callback_query(F.data.startswith('select_post_'))
async def show_select_post(call: CallbackQuery, state: FSMContext):
    """Функция для получения выбранной Статьи"""
    await call.answer()
    await state.clear()
    sel_title = call.data.replace('select_post_', '')
    sel_post = await get_post(post_title=sel_title)
    if sel_post:
        await send_post(bot, user_id=call.from_user.id, all_news=sel_post)

'''
@show_news_router.message(F.text == '📋 Просмотр местоположений')
async def start_views_noti(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Выбери какие заметки отобразить', reply_markup=find_note_kb())

'''
