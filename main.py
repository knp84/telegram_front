import  asyncio 
from asyncpg_lite import DatabaseManager
from decouple import config
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.middlewares import DatabaseMiddleware
from config import API_TOKEN
DATABASE_URL = 'postgresql://postgres:4012009@localhost:5432/test_db'
pg_manager = DatabaseManager(dsn=config(DATABASE_URL), deletion_password=config('4012009'))

async def main():
   bot = Bot(token=API_TOKEN)
   dp = Dispatcher()
   dp.include_router(router)
   await bot.delete_webhook(drop_pending_updates=True)
   await dp.start_polling(bot)


if __name__ == '__main__':
   try:   
      asyncio.run(main())
   except KeyboardInterrupt:
      print('бот выключен')   