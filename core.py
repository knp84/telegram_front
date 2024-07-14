from math import sqrt
from random import randint
def player_solution():
    match determine:                                 #определяет какой тип нужно проверять
        case 1:
            try:
                solution = int(input())                                    
            except:                                                            
                return print('Ошибка ввода! Введите число!')                
        case 2:
            try:
                solution = float(input('округлите x до первого знака после запятой '))
            except:
                print('Введите число с плавающей точкой!')
        case 3:
            solution = input()
            try:
                int(solution)
            except:
                print('Введите строковое значение')
    return solution

                               
a = randint(0,100)
b = randint(0,100)
c = randint(0,10)
d = randint(0,10)
determine = 1
addition_plus = a + b
addition_player = str(addition_plus)
plus = (f'Введите сумму чисел {a} и {b}: ')
pon_1 = (f'да, {a} + {b} = {addition_plus}')         

pon = ('Неверный ответ!')  
print(addition_player)

multyplie = d * c
multyplie_player = str(multyplie)
plus_1 = (f'Введите произведение чисел {d} и {c}: ')
pon_2 = (f'да, {d} * {c} = {multyplie}')   