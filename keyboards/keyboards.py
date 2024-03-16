from aiogram import types


button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/flower')
button3 = types.KeyboardButton(text='Инфо')
button4 = types.KeyboardButton(text='Покажи лису')
button5 = types.KeyboardButton(text='Закрыть')
buttonMy1 = types.KeyboardButton(text='/story')
buttonMy2 = types.KeyboardButton(text='Погода')
buttonMy3 = types.KeyboardButton(text='/date')

keyboard1 = [
    [button1, button2, button3],
    [button4, button5],
]

keyboard2 = [
    [button3, button4],
]

keyboard3 = [
    [buttonMy1, buttonMy2, buttonMy3, button5],
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)
kb3 = types.ReplyKeyboardMarkup(keyboard=keyboard3, resize_keyboard=True)