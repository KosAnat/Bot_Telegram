from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from Game_API import working_with_the_api
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


async def send_welcome(message: types.Message):
    try:
        await bot.send_message(message.from_user.id,
                               "Привет!\nЯ GameBot!\nОтправь мне любое сообщение, а я тебе обязательно отвечу.",
                               reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через лс, напишите ему:\nhttps://t.me/All_about_game_bot')


class FSM_all_game(StatesGroup):
    searching_game = State()
    info_game = State()





async def all_game(message: types.Message):
    await FSM_all_game.searching_game.set()
    await message.reply(
        "Введите игру или часть названия игры, чтобы найти ее полное название\n Например:\n Вы хотите найти игру Grand Theft Auto V."
        " Отправьте: Grand \n И бот обязательно отправит вам список игр, которые начинаются на 'Grand'!")


@dp.message_handler(content_types=['text'], state=FSM_all_game.searching_game)
async def search_and_send_game(message: types.Message, state: FSMContext):
    for game in working_with_the_api.search_game(message.text):
        await bot.send_message(message.from_user.id, game)
    await message.reply('Поиск закончен')

    await state.finish()

async def full_game(message: types.Message):
    await FSM_all_game.info_game.set()
    await message.reply(
        "Введите название игры, о которой хотите получить полную информацию")

@dp.message_handler(state=FSM_all_game.info_game)
async def search_and_send_game(message: types.Message, state: FSMContext):
    game = working_with_the_api.all_about_game(message.text)
    await bot.send_message(message.from_user.id, game)

    await state.finish()

def register_handers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(all_game, commands=['Найти_игру'], state=None)
    dp.register_message_handler(full_game, commands=['Информация_о_игре'],state=None)