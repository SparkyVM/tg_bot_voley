from aiogram import types


def make_row_keyboard(items: list[str]) -> types.ReplyKeyboardMarkup:
    row = [types.KeyboardButton(text=item) for item in items]           # Создание кнопок на основе переданного Листа
    return types.ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)  # Возвращаем созданную клаву