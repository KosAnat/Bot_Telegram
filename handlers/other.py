from aiogram import types, Dispatcher
from create_bot import dp
import json, string



async def swearing(message: types.Message):
    word = {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in
            message.text.split(' ')}.intersection(
        set(json.load(open('cenz.json'))))
    if word != set():
        await message.reply('Мат запрещен!')
        await message.delete()

def register_handers_other(dp: Dispatcher):
    dp.register_message_handler(swearing)