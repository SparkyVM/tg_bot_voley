from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import date, timedelta


    #Inline version

def generate_news_kb(news):
    unique_news = {post['title'] for post in news}
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for post_title in unique_news:
        button = InlineKeyboardButton(text=post_title, callback_data=f"select_post_{post_title}")
        keyboard.inline_keyboard.append([button])

    keyboard.inline_keyboard.append([InlineKeyboardButton(text="Главное меню", callback_data="main_menu")])

    return keyboard


def generate_locations_kb(locations):
    unique_location = {location['name'] for location in locations}
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for name_loc in unique_location:
        button = InlineKeyboardButton(text=name_loc, callback_data=f"select_loc_{name_loc}")
        keyboard.inline_keyboard.append([button])

    keyboard.inline_keyboard.append([InlineKeyboardButton(text="Главное меню", callback_data="main_menu")])

    return keyboard


def generate_courts_kb(courts):
    unique_court = {court['court_name'] for court in courts}
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for name_court in unique_court:
        button = InlineKeyboardButton(text=name_court, callback_data=f"select_court_{name_court}")
        keyboard.inline_keyboard.append([button])

    keyboard.inline_keyboard.append([InlineKeyboardButton(text="Главное меню", callback_data="main_menu")])

    return keyboard


def generate_date_kb():
    unique_dates = {(date.today()+timedelta(days=i)).strftime('%d.%m') for i in range(0, 3)}
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    for date_res in unique_dates:
        button = InlineKeyboardButton(text=date_res, callback_data=f"select_date_{date_res}")
        keyboard.inline_keyboard.append([button])

    keyboard.inline_keyboard.append([InlineKeyboardButton(text="Главное меню", callback_data="main_menu")])

    return keyboard