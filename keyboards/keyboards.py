from aiogram import types


button1 = types.KeyboardButton(text='/новости')
button2 = types.KeyboardButton(text='/соревнования')
button3 = types.KeyboardButton(text='/бронь')
button4 = types.KeyboardButton(text='/адреса')
button5 = types.KeyboardButton(text='О нас')
buttonPlay1 = types.KeyboardButton(text='/участвовать')
buttonPlay2 = types.KeyboardButton(text='/выход')

keyboardStart = [
    [button1, button2, button3],
    [button4, button5],
]

keyboardPlay = [
    [buttonPlay1, buttonPlay2],
]


kbMain = types.ReplyKeyboardMarkup(keyboard=keyboardStart, resize_keyboard=True)
kbPlay = types.ReplyKeyboardMarkup(keyboard=keyboardPlay, resize_keyboard=True)