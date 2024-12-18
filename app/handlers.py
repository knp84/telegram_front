from aiogram import  Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command


from app.keyboard import main, Levels

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import core

router = Router()

class CallbackQuery(StatesGroup):
   level_1 = State()
   level_2 = State()
   level_3 = State()
   level_4 = State()

class Stopping(StatesGroup):
   stop = State()
   resume = State()

@router.message(CommandStart())
async def send_welcome(message: Message):
   await message.answer("Начало работы \nВыберите уровень сложности", reply_markup=main)
   

@router.message(Command('stop'))
async def Stop(message: Message,state: FSMContext):
   await message.answer('ok')
   await state.set_state(Stopping.stop)
   

@router.message(F.text=='Выбрать уровень сложности')
async def levels_dif(message: Message):
   await message.answer('difficulty levels', reply_markup=Levels)

   
@router.callback_query(F.data == 'level_one')               #даю сатусы
async def level_one(callback: CallbackQuery, state: FSMContext):    
   
   await callback.answer('Уровень 1: Cложение')
   await callback.message.answer(core.question_plus)
   await state.set_state(CallbackQuery.level_1)
   
   
      

   
@router.callback_query(F.data == 'level_two')
async def level_two(callback: CallbackQuery, state: FSMContext):      
   await callback.answer('Уровень 2: Умножение')
   await callback.message.answer(core.question_multiply) 
   await state.set_state(CallbackQuery.level_2)

@router.message(CallbackQuery.level_1)                #реагирую на статусы
async def level_1(message: Message, state: FSMContext):
   await state.update_data(level_1=message.text)

   if message.text in core.spisok_str:
      if message.text == core.plus:
         await message.answer(core.correct_result_plus)
      else:
         await message.answer(core.wrong_result)
   else:
      await message.answer('Введите число!')
      
   await state.set_state(Stopping.resume)
   await message.answer('Продолжить? да/нет')
   

   
@router.message(CallbackQuery.level_2)
async def level_2(message: Message, state: FSMContext):
   await state.update_data(level_2=message.text)
   
   if message.text in core.spisok_str:
      if message.text == core.multiply:
         await message.answer(core.correct_result_multiply)
      else:
         await message.answer(core.wrong_result)
   else:
      await message.answer('Введите число!')
   
   await state.set_state(Stopping.resume)
   await message.answer('Продолжить? да/нет')

#level_3 and level_4 later

@router.message(Stopping.resume)
async def Resume(message: Message, state: FSMContext):
   
   if message.text == 'нет':
      await state.set_state(Stopping.stop)

   elif message.text == 'да':
      await message.answer('difficulty levels', reply_markup=Levels)






