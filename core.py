from math import sqrt
from random import randint
                           
a = randint(0,100)
b = randint(0,100)

plus = a + b
plus = (f'Введите сумму чисел {a} и {b}: ')

correct_result_plus = (f'да, {a} + {b} = {plus}')         
wrong_result = ('Неверный ответ!')  

print(plus)


c = randint(0,10)
d = randint(0,10)

multiply = d * c
plus_1 = (f'Введите произведение чисел {d} и {c}: ')
correct_result_multiply = (f'да, {d} * {c} = {multiply}')   