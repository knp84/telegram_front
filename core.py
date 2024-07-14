from math import sqrt
from random import randint

one_to_ten = str(range(1,11))

a = randint(0,100)
b = randint(0,100)

plus = str(a + b)
question_plus = (f'Введите сумму чисел {a} и {b}: ')

correct_result_plus = (f'да, {a} + {b} = {plus}')         


print(plus)


c = randint(0,10)
d = randint(0,10)

multiply = d * c
question_multiply = (f'Введите произведение чисел {d} и {c}: ')
correct_result_multiply = (f'да, {d} * {c} = {multiply}')   


wrong_result = ('Неверный ответ!')  

print(one_to_ten)