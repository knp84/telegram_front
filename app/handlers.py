from aiogram import  Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from app.keyboard import main, Levels

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from random import randint

router = Router()

class CallbackQuery(StatesGroup):
   level_1 = State()
   level_2 = State()
   level_3 = State()
   level_4 = State()

def player_solution(mark):
   a = randint(0,100)
   b = randint(0,100)
   if mark == 1:
      plus = str(a + b)
      question_plus = (f'Введите сумму чисел {a} и {b}: ')
      correct_result_plus = (f'да, {a} + {b} = {plus}')      
      return plus, question_plus, correct_result_plus
   elif mark == 2:
      a = randint(0,10)
      b = randint(0,100)
      multiply = str(a * b)
      question_multiply = (f'Введите произведение чисел {a} и {b}: ')
      correct_result_multiply = (f'да, {a} * {b} = {multiply}')
      return multiply, question_multiply, correct_result_multiply
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
   global plus, correct_result_plus
   plus, question_plus, correct_result_plus = player_solution(1)
   await callback.answer('Уровень 1: Cложение')
   await callback.message.answer(question_plus)
   await state.set_state(CallbackQuery.level_1)
   
   
      

   
@router.callback_query(F.data == 'level_two')
async def level_two(callback: CallbackQuery, state: FSMContext):      
   global multiply, correct_result_multiply
   multiply, question_multiply, correct_result_multiply = player_solution(2)
   await callback.answer('Уровень 2: Умножение')
   await callback.message.answer(question_multiply) 
   await state.set_state(CallbackQuery.level_2)


@router.message(CallbackQuery.level_1)                #реагирую на статусы
async def level_1(message: Message, state: FSMContext):
   await state.update_data(level_1=message.text)

   if message.text in [str(i) for i in range(0,99999)]:
      if message.text == plus:
         await message.answer(correct_result_plus)
      else:
         await message.answer('Неверный ответ!')
   else:
      await message.answer('Введите число!')
      
   await state.set_state(Stopping.resume)
   await message.answer('Продолжить? да/нет')
   

   
@router.message(CallbackQuery.level_2)
async def level_2(message: Message, state: FSMContext):
   await state.update_data(level_2=message.text)
   
   if message.text in [str(i) for i in range(0,99999)]:
      if message.text == multiply:
         await message.answer(correct_result_multiply)
      else:
         await message.answer('Неверный ответ!')
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






