from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.din_keyboards import make_row_keyboard
from keyboards.keyboards import kbMain
from datetime import datetime,timedelta



router = Router()           # Объявили Роутер


available_locations = ["Партизан", "Самара Арена", "Восход"]     
available_courts = ["1", "2", "3", "4", "5"]
available_date = [ (datetime.today() + timedelta(days=i+1)).strftime('%d.%m') for i in range(5)]
available_time = ["Утро", "День", "Вечер"]                  


class ChoiceVoleyCourt(StatesGroup):                     # Класс для сохранения состояния объекта
    choice_locations = State()
    choice_courts = State()
    choice_date = State()
    choice_time = State()


#Хэндлер на команду /reg
@router.message(Command('reg'))
@router.message(Command('бронь'))
async def cmd_reg_court(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(
        f'Выберите удобное расположение:',
        reply_markup=make_row_keyboard(available_locations)
    )
    await state.set_state(ChoiceVoleyCourt.choice_locations)


# Сохранение выбранного местоположения
@router.message(ChoiceVoleyCourt.choice_locations, F.text.in_(available_locations))
async def location_chosen(message: types.Message, state: FSMContext):
    await state.update_data(chosen_loc=message.text.lower())
    await message.answer(
        text='Хорошо, теперь выберем корт:',
        reply_markup=make_row_keyboard(available_courts)
    )
    await state.set_state(ChoiceVoleyCourt.choice_courts)

# Обработка если нет выбранного местоположения
@router.message(ChoiceVoleyCourt.choice_locations)
async def location_chosen_incorrectly(message: types.Message):
    await message.answer(
        'Выберите другой вариант1',
        reply_markup=make_row_keyboard(available_courts)
    )


# Сохранение выбранного корта
@router.message(ChoiceVoleyCourt.choice_courts, F.text.in_(available_courts))
async def court_chosen(message: types.Message, state: FSMContext):
    await state.update_data(chosen_court=message.text.lower())
    await message.answer(
        text='Выберите дату:',
        reply_markup=make_row_keyboard(available_date)
    )
    await state.set_state(ChoiceVoleyCourt.choice_date)

# Обработка если нет выбранного корта
@router.message(ChoiceVoleyCourt.choice_courts)
async def court_chosen_incorrectly(message: types.Message):
    await message.answer(
        'Выбери другой вариант2',
        reply_markup=make_row_keyboard(available_courts)
    )


# Сохранение выбранной даты
@router.message(ChoiceVoleyCourt.choice_date, F.text.in_(available_date))
async def date_chosen(message: types.Message, state: FSMContext):
    await state.update_data(chosen_date=message.text.lower())
    await message.answer(
        text='Выберите удобное время:',
        reply_markup=make_row_keyboard(available_time)
    )
    await state.set_state(ChoiceVoleyCourt.choice_time)

# Обработка если нет выбранной даты
@router.message(ChoiceVoleyCourt.choice_date)
async def date_chosen_incorrectly(message: types.Message):
    await message.answer(
        'Выбери другой вариант3',
        reply_markup=make_row_keyboard(available_date)
    )


# Сохранение выбранного времени
@router.message(ChoiceVoleyCourt.choice_time, F.text.in_(available_time))
async def time_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        f'Ждем вас {message.text.lower()} {user_data.get("chosen_date")} на {user_data.get("chosen_loc")} - {user_data.get("chosen_court")} корт.',
        #reply_markup=types.ReplyKeyboardRemove()
        reply_markup=kbMain
    )
    await state.clear()

# Обработка если нет выбранного времени
@router.message(ChoiceVoleyCourt.choice_time)
async def time_chosen_incorrectly(message: types.Message):
    await message.answer(
        'У нас нет такого варианта',
        reply_markup=make_row_keyboard(available_time)
    )
""" 
#Хендлер на сообщения
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'Запись' in msg_user:
        await cmd_registration(message)
 """