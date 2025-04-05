from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

btNews = KeyboardButton(text='/новости')
btTrnt = KeyboardButton(text='/соревнования')
btReserve = KeyboardButton(text='/бронь')
btContact = KeyboardButton(text='/адреса')
btAbout = KeyboardButton(text='О нас')
btPlay = KeyboardButton(text='/участвовать')
btExit = KeyboardButton(text='/выход')

kb_start = [
    [btNews, btTrnt, btReserve],
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


def stop_fsm():
    kb_list = [
        [KeyboardButton(text="❌ Остановить сценарий")],
        [KeyboardButton(text="🏠 Главное меню")]
    ]

    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Для того чтоб остановить сценарий FSM нажми на одну из двух кнопок👇"
    )

def news1_kb():
    kb_news1 = [
        [KeyboardButton(text="Открыть новость 1")],
        [KeyboardButton(text="🏠 Главное меню")]
    ]

    return ReplyKeyboardMarkup(
        keyboard=kb_news1,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйся меню👇"
    )