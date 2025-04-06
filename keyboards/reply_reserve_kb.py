from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

btTime9 = KeyboardButton(text='9:00')
btTime11 = KeyboardButton(text='11:00')
btTime13 = KeyboardButton(text='13:00')
btTime15 = KeyboardButton(text='15:00')
btTime17 = KeyboardButton(text='17:00')
btTime19 = KeyboardButton(text='19:00')


def reserve_start():
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

def reserve_time():
    kb_time = [
        [btTime9, btTime11, btTime13,btTime15, btTime17, btTime19],
        [KeyboardButton(text="Другая дата"),KeyboardButton(text="🏠 Главное меню")]
    ]

    return ReplyKeyboardMarkup(
        keyboard=kb_time,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )