from aiogram import  Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from app.keyboard import main

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import okPon

router = Router()

class Playing(StatesGroup):
   level_1 = State()
   level_2 = State()
   level_3 = State()
   level_4 = State()

@router.message(CommandStart())
async def send_welcome(message: Message):
   await message.answer("Начало работы \nВыберите уровень сложности", reply_markup=main)

@router.message(F.text == 'Уровень 1')
async def addition_plus(message: Message, state: FSMContext):
   await state.set_state(Playing.level_1)
   await message.answer(okPon.plus)

@router.message(Playing.level_1)
async def level_1(message: Message, state: FSMContext):
   await state.update_data(level_1=message.text)

   if message.text == okPon.addition_player:
      await message.answer(okPon.pon_1)
   else:
      await message.answer(okPon.pon)
