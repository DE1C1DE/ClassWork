def func():
    a=float(input())
    b=float(input())
    if a>b:
        print(a-b)
    else:
        print(b-a)
    return a,b 
c, d=func()
e, f=func()
z, x=func()

#Задача 1 и 2

def Func1(a,b,c):
    d=a+b+c   
    print(d)    
def Func2(a,b,c):
    d=a-b-c
    print(d)
print("Что нужно сделать?")
print("1 - Сложить, 2 - Вычесть")
var=int(input())
if var == 1:
    print("Введите число 1 >>> ")
    a=int(input())
    print("Введите число 2 >>> ")
    b=int(input())
    print("Введите число 3 >>> ")
    c=int(input())
    Func1(a, b, c)
elif var == 2:
    print("Введите число 1 >>> ")
    a=int(input())
    print("Введите число 2 >>> ")
    b=int(input())
    print("Введите число 3 >>> ")
    c=int(input())
    Func2(a, b, c)
else:
    print("Введено неверное действие")
