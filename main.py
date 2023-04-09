from aiogram import executor
from create_bot import dp

async def on_startup(_):
    print('Бот вышел в онлайн')

from handlers import client, admin, other

client.register_handers_client(dp)
other.register_handers_other(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

