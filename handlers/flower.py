from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.flower_keyboards import make_row_keyboard



router = Router()           # Объявили Роутер


available_persons = ["девушка", "родственник", "коллега"]       # Лист. Возмодные профессии
available_flower_type = ["розы", "тюльпаны", "альстромерия", "ромашки"] 
available_flower_size = ["маленький", "средний", "большой"]                  # Лист. Возможные уровни


class ChoiceFlowerNames(StatesGroup):                     # Класс для сохранения состояния объекта
    choice_persons = State()
    choice_flower_type = State()
    choice_flower_size = State()


#Хэндлер на команду /flower
@router.message(Command('flower'))
async def cmd_flower(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(
        f'Приветствуем в цветочном магазине! Для кого выбираем букет?',
        reply_markup=make_row_keyboard(available_persons)
    )
    await state.set_state(ChoiceFlowerNames.choice_persons)


# Сохранение выбранной персоны
@router.message(ChoiceFlowerNames.choice_persons, F.text.in_(available_persons))
async def person_chosen(message: types.Message, state: FSMContext):
    await state.update_data(chosen_pers=message.text.lower())
    await message.answer(
        text='Хорошо, из каких цветов собирать букет?',
        reply_markup=make_row_keyboard(available_flower_type)
    )
    await state.set_state(ChoiceFlowerNames.choice_flower_type)

# Обработка если нет выбранной персоны
@router.message(ChoiceFlowerNames.choice_persons)
async def person_chosen_incorrectly(message: types.Message):
    await message.answer(
        'Выбери другой вариант 1',
        reply_markup=make_row_keyboard(available_persons)
    )


# Сохранение выбранных цветов
@router.message(ChoiceFlowerNames.choice_flower_type, F.text.in_(available_flower_type))
async def type_chosen(message: types.Message, state: FSMContext):
    await state.update_data(chosen_type=message.text.lower())
    await message.answer(
        text='Какой размер букета ?',
        reply_markup=make_row_keyboard(available_flower_size)
    )
    await state.set_state(ChoiceFlowerNames.choice_flower_size)

# Обработка если нет выбранных цыетов
@router.message(ChoiceFlowerNames.choice_flower_type)
async def type_chosen_incorrectly(message: types.Message):
    await message.answer(
        'Выбери другой вариант 2',
        reply_markup=make_row_keyboard(available_flower_type)
    )


# Сохранение выбранного размера
@router.message(ChoiceFlowerNames.choice_flower_size, F.text.in_(available_flower_size))
async def size_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        f'Вы выбрали {message.text.lower()} букет из {user_data.get("chosen_type")} для {user_data.get("chosen_pers")}. Уже собираем букет )',
        reply_markup=types.ReplyKeyboardRemove()
    )
    await state.clear()

# Обработка если нет выбранного уровня
@router.message(ChoiceFlowerNames.choice_flower_size)
async def size_chosen_incorrectly(message: types.Message):
    await message.answer(
        'У нас нет такого варианта',
        reply_markup=make_row_keyboard(available_flower_size)
    )