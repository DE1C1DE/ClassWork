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

