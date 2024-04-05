from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.din_keyboards import make_row_keyboard
from keyboards.keyboards import kbMain, kbPlay
from datetime import datetime,timedelta

router = Router()

date_plays = [ (datetime.today() + timedelta(days=i+1)).strftime('%d.%m') for i in range(6,22,7)]
name_plays = ['Первенство города Самара','Кубок летчиков','Спартакиада']
available_age_category = ['дети','взрослые','ветераны']
news_iter = 0
news_list = []


class ChoicePlay(StatesGroup):                     # Класс для сохранения состояния объекта
    choice_date = State()
    choice_age_category = State()

with open('news_txt.txt', encoding='utf-8') as f:
    news_list = f.readlines()


#Хэндлер на команду /news
@router.message(Command('news'))
@router.message(Command('новости'))
async def cmd_news(message: types.Message):
    with open('news_txt.txt', encoding='utf-8') as f:
        global news_iter, news_list
        if news_iter > 2:
            news_iter =0
        text = news_list[news_iter]
        news_iter += 1
        await message.answer(f'Новости:\n\n{text}', reply_markup=kbMain)
 
#Хэндлер на команду /plays
@router.message(Command('plays'))
@router.message(Command('соревнования'))
async def cmd_plays(message: types.Message):
    plays_text = ''
    for i in range(len(date_plays)):
        plays_text = plays_text + f'{date_plays[i]} - {name_plays[i]} \n'
    await message.answer(f'Ближайшие соревнования:\n\n{plays_text}', reply_markup=kbPlay)

#Хэндлер на команду /выход
@router.message(Command('выход'))
async def cmd_start(message: types.Message):
    await message.answer('Выход в основное меню...', reply_markup=kbMain)

            # ---- интерактивный режим ------------------------
    
#Хэндлер на команду /участвовать
@router.message(Command('участвовать'))
async def cmd_reg_play(message: types.Message, state: FSMContext):
    await message.answer(
        f'Выберите дату соревнования:',
        reply_markup=make_row_keyboard(date_plays)
    )
    await state.set_state(ChoicePlay.choice_date)


# Сохранение выбранной даты соревнования
@router.message(ChoicePlay.choice_date, F.text.in_(date_plays))
async def date_play_chosen(message: types.Message, state: FSMContext):
    await state.update_data(chosen_date_play=message.text.lower())
    await message.answer(
        text='Выберите возрастную категорию:',
        reply_markup=make_row_keyboard(available_age_category)
    )
    await state.set_state(ChoicePlay.choice_age_category)

# Обработка если нет выбранной даты соревнования
@router.message(ChoicePlay.choice_date)
async def date_play_chosen_incorrectly(message: types.Message):
    await message.answer(
        'Выберите из доступных дат:',  
        reply_markup=make_row_keyboard(date_plays)
    )


# Сохранение выбранного категории
@router.message(ChoicePlay.choice_age_category, F.text.in_(available_age_category))
async def age_category_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    chosen_cup = name_plays[date_plays.index(user_data.get("chosen_date_play"))]
    await message.answer(
        f'Вы подали заявку на участие в {chosen_cup} ({user_data.get("chosen_date_play")}) в возрастной категории: {message.text.lower()}.',
        #reply_markup=types.ReplyKeyboardRemove()
        reply_markup=kbMain
    )
    await state.clear()

# Обработка если нет выбранного категории
@router.message(ChoicePlay.choice_age_category)
async def age_category_chosen_incorrectly(message: types.Message):
    await message.answer(
        'Выберите из предложенных категорий:',
        reply_markup=make_row_keyboard(available_age_category)
    )

