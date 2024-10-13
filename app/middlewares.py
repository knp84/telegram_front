from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from app.handlers import level_1, CallbackQuery

class TestMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[CallbackQuery, level_1]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[CallbackQuery, level_1]
    ) -> Any:
        print('123')
        return await handler(event, data)