from math import sqrt
from random import randint

spisok= list(range(0,99999)) #ничего лучше в голову не лезет
spisok_str = str(spisok)


#позже попытаюсь сделать базу данных(если мне это чем то поможет), а пока что просто не могу ввести разнообразие примеров
class AB():
    a = randint(0,100)
    b = randint(0,100)
    plus = str(a + b)
    def reload_ab(z):
        AB.a += randint(0,50)
        AB.b += randint(0,50)
        if z == 'a':
            print(AB.a)
            return AB.a
        elif z == 'b':
            return AB.b





question_plus = (f'Введите сумму чисел {AB.a} и {AB.b}: ')
correct_result_plus = (f'да, {AB.a} + {AB.b} = {AB.plus}') 

       
print(question_plus)    
print(correct_result_plus)
    





c = randint(0,10)
d = randint(0,10)

multiply = str(d * c)
question_multiply = (f'Введите произведение чисел {d} и {c}: ')
correct_result_multiply = (f'да, {d} * {c} = {multiply}')   


wrong_result = ('Неверный ответ!')  
