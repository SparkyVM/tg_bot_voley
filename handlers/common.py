from aiogram import types, F, Router
from aiogram.filters.command import Command
from keyboards.keyboards import kbMain
#from handlers.registration import cmd_registration
from handlers.news import cmd_news, cmd_plays
from utils.random_fox import fox


router = Router()


#Хэндлер на команду /start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'{name}, приветствуем вас на кортах "Остров"', reply_markup=kbMain)


#Хэндлер на команду /stop
@router.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Ждем вас снова, {name}')


#Хэндлер на команду /location
@router.message(Command('location'))
async def cmd_location(message: types.Message):
    loc1 = 'Манеж "Партизан"\n Самара, Партизанская улица, 17с4\n +7 (846) 611 90 09' 
    loc2 = 'Самара Арена\n Самара, Волжское шоссе, 100\n +7 (846) 622 90 09'
    loc3 = 'Манеж "Восход"\n Самара, Самара, улица Калинина, 23\n +7 (846) 633 90 09'
    await message.answer(f'Наши адреса:\n\n - {loc1}\n\n - {loc2}\n\n - {loc3}')

#Хэндлер на команду /about
@router.message(Command('about'))
async def cmd_about(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Мы сеть кортов для занятия пляжным волейболом "Остров"')

@router.message(Command('fox'))
@router.message(Command('лиса'))
@router.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}')
    await message.answer_photo(photo=img_fox)
    # await message.answer_
    # await bot.send_photo(message.from_user.id, photo=img_fox)



#Хендлер на сообщения
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Рад тебя видеть, {name}')
    elif 'ты кто' in msg_user:
        await message.answer(f'Я аЛиса, ваш не голосовой помощник )')
    elif 'лис' in msg_user:
        await message.answer(f'Смотри что у меня есть, {name}', reply_markup=kbMain)
    elif 'адреса' in msg_user:
        await cmd_location(message)
    elif 'стоп' in msg_user:
        await cmd_stop(message)
    else:
        await message.answer(f'Я не знаю такой команды')