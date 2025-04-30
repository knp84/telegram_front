import  asyncio 
from aiogram import Bot, Dispatcher

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.handlers import router
from app.middlewares import DatabaseMiddleware
from config import API_TOKEN, load_config, Config




async def main():
   config: Config = load_config()
   engine = create_async_engine(url=config.db.url, echo=True)
   session = async_sessionmaker(engine, expire_on_commit=False)
   
   bot = Bot(token=API_TOKEN, parse_mode='HTML')
   dp = Dispatcher()
   dp.include_router(router)
   dp.update.middleware(DatabaseMiddleware(session=session))
   await bot.delete_webhook(drop_pending_updates=True)
   await dp.start_polling(bot)
   

if __name__ == '__main__':
   try:   
      asyncio.run(main())
   except KeyboardInterrupt:
      print('бот выключен')   