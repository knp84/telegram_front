from random import randint

spisok= list(range(0,99999)) #ничего лучше в голову не лезет
spisok_str = str(spisok)


a = randint(0,100)
b = randint(0,100)
    

plus = str(a + b)
question_plus = (f'Введите сумму чисел {a} и {b}: ')
correct_result_plus = (f'да, {a} + {b} = {plus}')   





#не могу ввести разнообразие примеров


c = randint(0,10)
d = randint(0,10)

multiply = str(d * c)
question_multiply = (f'Введите произведение чисел {d} и {c}: ')
correct_result_multiply = (f'да, {d} * {c} = {multiply}')   


wrong_result = ('Неверный ответ!')  
