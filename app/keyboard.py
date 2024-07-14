from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text='Выбрать уровень сложности')]],
                        resize_keyboard=True)

Levels = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Уровень 1', callback_data='level_one')],
    [InlineKeyboardButton(text='Уровень 2', callback_data='level_two')]])

                                               