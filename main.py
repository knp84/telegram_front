import  asyncio 
from aiogram import Bot, Dispatcher
from app.handlers import router

async def main():
   bot = Bot(token='7385612852:AAGR89iMdDo4mN8x1TONa7XQzV_00avuzS0')
   dp = Dispatcher()
   dp.include_router(router)
   await dp.start_polling(bot)

if __name__ == '__main__':
   try:   
      asyncio.run(main())
   except KeyboardInterrupt:
      print('бот выключен')   