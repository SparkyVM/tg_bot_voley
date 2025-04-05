from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from data_base.dao import get_about
from keyboards.reply_menu_kb import main_kb


show_info_router = Router()


class FindNoteStates(StatesGroup):
    text = State()  # Ожидаем любое сообщение от пользователя


@show_info_router.message(F.text == 'О нас')
async def info_about(message: Message, state: FSMContext):
    """Функция получения информации о Компании"""
    await state.clear()
    about_text = await get_about()
    if about_text:
        await message.answer('О нас:\n'+str(about_text), reply_markup=main_kb())
    else:
        await message.answer('Информация отсутствует', reply_markup=main_kb())