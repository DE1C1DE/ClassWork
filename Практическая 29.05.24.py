# Задание 1
while True:
    a = input('Введите число >>> ')
    try:
            a=int(a)
            for i in range(a+1):
                    print(i, end="")
            break
    except ValueError:
            print(a,' - не число. Повторите ввод')
#Задание 2
array=[1, 5, 7, 13]
for i in array:
    try:
        print(i/array.index(i))
    except ZeroDivisionError:
        print('Деление на 0!', i)
#Задание 3
array=[]
count=0
while count!=5:
    elem=input('Введите число >>> ')
    try:
        elem=int(elem)
        array.append(elem)
        count+=1
    except ValueError:
        count+=0
print(array)

#Задание 1 (Запросы в интернет)
import webbrowser
import urllib.request
a=False
browser={1: 'https://www.google.ru/search?q=', 2: 'https://ya.ru/search/?text='}
try:
    urllib.request.urlopen("http://google.com")
    print("Вы поодключены к сети")
    while a!=True:
        inp=int(input('Выберите поисковик \n1 - Google, 2 - Yandex\n>>> '))
        if inp == 1 or inp == 2:
            a=True
        else:
            print('\nВыберите из предложеных вариантов\n')
    question=input('Введите запрос\n>>> ')
    webbrowser.open(f'{browser[inp]}{question}')

except IOError:
    print("Вы не подключены к сети")
