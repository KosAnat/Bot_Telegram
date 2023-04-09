from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/Найти_игру')
b3 = KeyboardButton('/Информация_о_игре')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)#Заменяет клавиатуру

kb_client.add(b1).insert(b2).insert(b3) # Добавляет кнопки

