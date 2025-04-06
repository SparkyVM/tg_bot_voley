import asyncio
from keyboards.reply_menu_kb import main_kb
from keyboards.gen_other_kb import generate_courts_kb,generate_date_kb
from keyboards.reply_reserve_kb import reserve_time


async def send_message_user(bot, user_id, content_text=None, kb=None):
    """Функция для вывода сообщения"""
    await bot.send_message(chat_id=user_id, text=content_text, reply_markup=kb)


async def send_news(bot, user_id, all_news):
    """Функция для вывода Новостей"""
    for post in all_news:
        try:
            await send_message_user(bot=bot,
                                    user_id=user_id,
                                    content_text=post['title'],
                                    kb=main_kb())     #rule_note_kb(loc['id']))
        except Exception as E:
            print(f'Error: {E}')
            await asyncio.sleep(2)
        finally:
            await asyncio.sleep(0.5)

async def send_post(bot, user_id, all_news):
    """Функция для вывода Статьи"""
    for post in all_news:
        try:
            await send_message_user(bot=bot,
                                    user_id=user_id,
                                    content_text=f'- {post['title']}\n{post['content']}',
                                    kb=main_kb())
        except Exception as E:
            print(f'Error: {E}')
            await asyncio.sleep(2)
        finally:
            await asyncio.sleep(0.5)

async def send_courts(bot, user_id, all_courts):
    """Функция для вывода Кортов"""
    try:
        await send_message_user(bot=bot,
                                user_id=user_id,
                                content_text=f'Выбери доступный корт:',
                                kb=generate_courts_kb(courts=all_courts))
    except Exception as E:
        print(f'Error: {E}')
        await asyncio.sleep(2)
    finally:
        await asyncio.sleep(0.5)
    '''
        for court in all_courts:                        # ПРОВЕРИТЬ НЕОБХОД
        try:
            await send_message_user(bot=bot,
                                    user_id=user_id,
                                    content_text=f'Выбери доступный корт:',
                                    kb=generate_courts_kb(courts=all_courts))
        except Exception as E:
            print(f'Error: {E}')
            await asyncio.sleep(2)
        finally:
            await asyncio.sleep(0.5)
    '''



async def send_date(bot, user_id ):
    ''' ^ all_date'''
    """Функция для вывода Времени"""
    #for res_date in all_date:
    try:
        await send_message_user(bot=bot,
                                user_id=user_id,
                                content_text=f'Выбери доступную дату:',
                                kb=generate_date_kb())
    except Exception as E:
        print(f'Error: {E}')
        await asyncio.sleep(2)
    finally:
        await asyncio.sleep(0.5)


async def send_time(bot, user_id, all_time):
    """Функция для вывода Времени"""
    for rev_time in all_time:
        try:
            await send_message_user(bot=bot,
                                    user_id=user_id,
                                    content_text=f'Выбери доступное время:',
                                    kb=reserve_time(all_time))
        except Exception as E:
            print(f'Error: {E}')
            await asyncio.sleep(2)
        finally:
            await asyncio.sleep(0.5)

async def send_reserves(bot, user_id, all_reserves):
    """Функция для вывода Броней"""
    for reserve in all_reserves:
        try:
            await send_message_user(bot=bot,
                                    user_id=user_id,
                                    content_text=f'- {reserve['title']}\n{reserve['content']}',
                                    kb=main_kb())
        except Exception as E:
            print(f'Error: {E}')
            await asyncio.sleep(2)
        finally:
            await asyncio.sleep(0.5)




''' Not Use

async def send_locations(bot, user_id, all_locations):
    """Функция для вывода Местоположений"""
    for loc in all_locations:
        try:
            await send_message_user(bot=bot,
                                    user_id=user_id,
                                    content_text=loc['name'],
                                    kb=main_kb())
        except Exception as E:
            print(f'Error: {E}')
            await asyncio.sleep(2)
        finally:
            await asyncio.sleep(0.5)
'''
