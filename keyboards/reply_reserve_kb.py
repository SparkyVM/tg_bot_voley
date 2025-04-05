from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
#---------------------
btNews = KeyboardButton(text='/новости')
btTrnt = KeyboardButton(text='/соревнования')
btReserve = KeyboardButton(text='/бронь')
btContact = KeyboardButton(text='/адреса')
btAbout = KeyboardButton(text='О нас')
btPlay = KeyboardButton(text='/участвовать')
btExit = KeyboardButton(text='/выход')

kb_start = [
    [btNews, btTrnt, btReserve, btReserve],
    [btContact, btAbout],
]



kbTestAdmin = [
    [KeyboardButton(text='новость')],
]

def main_kb():
    return ReplyKeyboardMarkup(
        keyboard=kb_start,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )


def start_res1():
    kb_res1 = [
        [KeyboardButton(text="📝 Зарезервировать"), KeyboardButton(text="📋 Вывести брони")],
        [KeyboardButton(text="🏠 Главное меню")]
    ]

    return ReplyKeyboardMarkup(
        keyboard=kb_res1,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )