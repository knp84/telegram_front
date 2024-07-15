from math import sqrt
from random import randint
from app.handlers import deter
spisok= list(range(0,99999)) #ничего лучше в голову не лезет
spisok_str = str(spisok)


#позже попытаюсь сделать базу данных(если мне это чем то поможет), а пока что просто не могу ввести разнообразие примеров
i = 5

def plus_func(z):
    a = randint(0,100)
    b = randint(0,100)
        
    plus = str(a + b)
    
    question_plus = (f'Введите сумму чисел {a} и {b}: ')

    correct_result_plus = (f'да, {a} + {b} = {plus}')

    print(plus)
    
    if z == 1:
        return question_plus
    elif z == 2:
        return correct_result_plus
    elif z == 3:
        return plus
        



c = randint(0,10)
d = randint(0,10)

multiply = str(d * c)
question_multiply = (f'Введите произведение чисел {d} и {c}: ')
correct_result_multiply = (f'да, {d} * {c} = {multiply}')   


wrong_result = ('Неверный ответ!')  
