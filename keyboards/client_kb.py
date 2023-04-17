from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b2 = KeyboardButton('/Найти_игру')
b3 = KeyboardButton('/custom')
b4 = KeyboardButton('/high')
b5 = KeyboardButton('/low')
b6 = KeyboardButton('/range')
b7 = KeyboardButton('/history')
b8 = KeyboardButton('/help')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)

kb_client.insert(b2).insert(b3).insert(b4).insert(b5).add(b6).insert(b7).insert(b8)

