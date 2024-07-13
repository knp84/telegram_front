from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text='Уровень 1')],
                                    [types.KeyboardButton(text='Уровень 2')],
                                    [types.KeyboardButton(text='Уровень 3 WIP'),
                                    types.KeyboardButton(text='уровень 4 WIP')]],
                        resize_keyboard=True,
                        input_field_placeholder='Выберите уровень сложности....')