#Задание 1
def sum1(start, end):
    if start >end:
        start, end = end, start
    result = int()
    for i in range(start, end + 1):
        result += i
    print(result)
sum1(2, 8)
#Задание 2
функция 1: 4
Функция 2: 4
Функция 3: Оштбка
#Задание 3
a, b, c= 1, 2, 3
def three_args(a, b, c):
    print(a, b, c)
three_args(a, b, c)
Задание 4:
Не вызывается метод. Что бы работало надо вместо
dt
написать
dt.now().time()
#Задание 5
import inspect
def pr(a, b, c):
    a=2
    print(a)
def insp():
    param_names = pr.__code__.co_varnames[:pr.__code__.co_argcount]
    print(param_names)
insp()
