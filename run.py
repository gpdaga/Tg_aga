

import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


from app.handlers import router
from app.database.models import async_main
load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    await async_main()
    dp.include_router(router )
    print('Starting Bot...')
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")

import asyncio
from app.database.models import async_main

async def main():
    await async_main()  # Создаём таблицы
    print("✅ Таблицы успешно созданы!")

asyncio.run(main())
