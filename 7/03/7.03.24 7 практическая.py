#2 задача
a=int(input())
b=int(input())
mas=[]
while a<b:
    a+=1
    mas.append(a)

print(mas)
#3 задача
a=int(input())
b=int(input())
mas=[]
while a<b:
    a+=1
    mas.append(a)
mas.sort(reverse=True)
print(mas)

#Задание 13
import random
def creatArray():
    r = 0
    x = 6
    y = 8
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(0,100))
            r += 1
    return array

a=creatArray()
print(a)
print(a.count(0))

#14 Задание


