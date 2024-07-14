import  asyncio 
from aiogram import Bot, Dispatcher
from app.handlers import router

async def main():
   bot = Bot(token='7358633837:AAF_Zr8dIQLiARt8jiJleHEy0c9cwH1DQS4')
   dp = Dispatcher()
   dp.include_router(router)
   await dp.start_polling(bot)

if __name__ == '__main__':
   try:   
      asyncio.run(main())
   except KeyboardInterrupt:
      print('бот выключен')   