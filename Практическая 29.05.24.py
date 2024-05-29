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
