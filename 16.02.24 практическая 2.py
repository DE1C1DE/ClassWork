a=int(input())
b=int(input())
if a>b:
    print(a, 'больше', b)
    print(b, 'меньше', a)
elif a=b:
    print('Ты чё, берега попутал, пёс?')
else:
    print(b, 'больше', a)
    print(a, 'меньше', b)


a=int(input("Сторона квадрата "))
b=int(input("Радиус круга "))
if a>b*2:
    print("Круг впишется")
else:
    print("Круг не пришется")

x=int(input())
if x<0:
    print('y = ', x**2)
else:
    print('y = ', 1/(x**2))

import math
a=int(input("Сторона квадрата"))
b=int(input("Радиус круга"))
d=math.sqrt(a**2)
if d>=b*2:
    print("Не впишется")
else:
    print('Впишется')
  a=int(input())
b=int(input())
if a>b:
    print(a, 'больше', b)
elif a=b:
    print('Ты чё, берега попутал, пёс?')
else:
    print(b, 'больше', a)

#задача 10
a=int(input())
b=int(input())
c=int(input())
d=int(input())
f=sorted([a, b, c, d])
print(f[-1]+f[-2])

#задача 11
dict1={1: 'Понедельник', 2:'Вторник', 3: 'Среда', 4: "Четверг", 5: "Пятница", 6:"Суббота", 7: "Воскресенье" }
a=int(input())
print(dict1[a])

#задача 9
a=int(input('Оклад'))
if a>5000:
    b=a*1.1
    print("Премия - 10%")
else:
    b=a*1.12
    print("Премия - 12%")
print(b)


