import  asyncio 
from aiogram import Bot, Dispatcher
from app.handlers import router
from app.middlewares import TestMiddleware
from config import API_TOKEN


router.message.middleware(TestMiddleware())

async def main():
   bot = Bot(token=API_TOKEN)
   dp = Dispatcher()
   dp.include_router(router)
   await dp.start_polling(bot)

if __name__ == '__main__':
   try:   
      asyncio.run(main())
   except KeyboardInterrupt:
      print('бот выключен')   