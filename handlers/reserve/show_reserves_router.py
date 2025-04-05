from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from create_bot import bot
from data_base.dao import get_reserves_by_user, get_locations, get_courts
from utils.utils import send_reserves, send_courts

from keyboards.reply_menu_kb import main_kb
from keyboards.reply_reserve_kb import start_res1
from keyboards.gen_other_kb import generate_locations_keyboard

show_reserves_router = Router()


class FindReservesStates(StatesGroup):
    text = State()  # Ожидаем любое сообщение от пользователя


@show_reserves_router.message(F.text == '/бронь')
async def start_views_reserves(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Выбери действие', reply_markup=start_res1())

@show_reserves_router.message(F.text == '📋 Вывести брони')
async def find_all_reserves(message: Message, state: FSMContext):
    await state.clear()
    all_reserves = await get_reserves_by_user(user_id=message.from_user.id)
    if all_reserves:
        await send_reserves(all_reserves, bot, message.from_user.id)
        await message.answer(f'Все ваши {len(all_reserves)} заметок отправлены!', reply_markup=main_kb())
    else:
        await message.answer('У вас пока нет ни одной брони!', reply_markup=main_kb())

@show_reserves_router.message(F.text == '📝 Зарезервировать')
async def send_reserve_loc(message: Message, state: FSMContext):
    """Функция вывода доступных местоположений"""
    await state.clear()
    all_locations = await get_locations()       # получить Местоположения
    if all_locations:
        await message.answer('Выбери местоположение корта:', reply_markup=generate_locations_keyboard(all_locations))
    else:
        await message.answer('Нет доступных местоположений', reply_markup=main_kb())

@show_reserves_router.callback_query(F.data.startswith('select_loc_'))
async def send_reserve_court(call: CallbackQuery, state: FSMContext):
    """Функция вывода доступных кортов"""
    await call.answer()
    await state.clear()
    sel_loc = call.data.replace('select_loc_', '')
    sel_courts = await get_courts(loc_name=sel_loc)
    if sel_courts:
        await send_courts(bot, user_id=call.from_user.id, all_courts=sel_courts)

'''
@show_reserves_router.callback_query(F.data.startswith('select_court_'))
async def send_reserve_time(call: CallbackQuery, state: FSMContext):
    """Функция вывода доступных кортов"""
    await call.answer()
    await state.clear()
    sel_loc = call.data.replace('select_loc_', '')
    sel_courts = await get_courts(loc_name=sel_loc)
    if sel_courts:
        await send_courts(bot, user_id=call.from_user.id, all_courts=sel_courts)
    all_courts = await get_courts()  # получить Местоположения
    if all_courts:
        await message.answer('Выбери местоположение корта:', reply_markup=generate_locations_keyboard(all_locations))
    else:
        await message.answer('Нет доступных местоположений', reply_markup=main_kb())
'''



'''
@show_reserves_router.message(F.text == '/бронь')
async def show_all_reserves(message: Message, state: FSMContext):
    """Функция для получения всех Новостей"""
    await state.clear()
    all_news = await get_news()
    if all_news:
        await message.answer('Новости:', reply_markup=generate_news_keyboard(all_news))
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
