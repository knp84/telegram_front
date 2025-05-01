from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, TelegramObject 

class TestMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        
        print('все ок')
    
        return await handler(event, data)
    
class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, session: async_sessionmaker[AsyncSession]) -> None:
        self.session = session
'''
    async def __call__(
        self, 
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject, 
        data: Dict[str, Any]) -> Any:

'''



    
    