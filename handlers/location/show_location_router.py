from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from data_base.dao import get_locations
from keyboards.reply_menu_kb import main_kb

show_loc_router = Router()


class FindNoteStates(StatesGroup):
    text = State()  # Ожидаем любое сообщение от пользователя


@show_loc_router.message(F.text == '/адреса')
async def all_views_locs(message: Message, state: FSMContext):
    """Функция для получения Местоположений"""
    await state.clear()
    all_locations = await get_locations()
    if all_locations:
        result = f'Наши адреса:'
        for loc in all_locations:
            result = result + f'\n\n - {loc['name']}\n{loc['adress']}\n{loc['phone_number']}'
        await message.answer(result, reply_markup=main_kb())
    else:
        await message.answer('Нет информации о местоположениях!', reply_markup=main_kb())