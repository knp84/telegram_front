from math import sqrt
from random import randint
spisok= list(range(0,99999)) #ничего лучше в голову не лезет
spisok_str = str(spisok)


a_0 = lambda: randint(0, 100)

def plus_pon_a():
    a = a_0()
    return a

def plus_pon_b():
    b = a_0
    return b


a_1 = plus_pon_a()
b_1 = plus_pon_b()
plus = str(a_1 + b_1)
print(plus)

question_plus = (f'Введите сумму чисел {a_1} и {b_1}: ')
print(question_plus)

correct_result_plus = (f'да, {a_1} + {b_1} = {plus}')   
print(correct_result_plus)


#позже попытаюсь сделать базу данных(если мне это чем то поможет), а пока что просто не могу ввести разнообразие примеров







c = randint(0,10)
d = randint(0,10)

multiply = str(d * c)
question_multiply = (f'Введите произведение чисел {d} и {c}: ')
correct_result_multiply = (f'да, {d} * {c} = {multiply}')   


wrong_result = ('Неверный ответ!')  
