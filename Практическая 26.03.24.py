# 27
a=[1, 2, 1, 2, 3, 4, 3, 2, 4, 2, 4, 6, 5, 7, 8, 9,6, 7, 8, 5, 3, 4, 5, 8, 6]
b=[2, 4, 5, 3, 2, 5, 6, 7, 8, 8, 4, 5, 6, 7, 8, 9, 2]
print(set(a+b))

#28
import random  
def creatArray():
    r = 0
    print('Input first index matrix: ')
    x = int(input())
    print('Input second index matrix: ')
    y = int(input())
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(0,100))
            r += 1  
    return array
matrix=creatArray()
count=0
for i in matrix:
    for n in i:
        if n != 0:
            count+=1
print(matrix)
print(count)

#29
import random  
def creatArray():
    r = 0
    print('Input first index matrix: ')
    x = int(input())
    print('Input second index matrix: ')
    y = int(input())
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(-100,100))
            r += 1  
    return array
D=creatArray()
proizv=1
for i in D:
    for n in i:
        if n < 0:
            proizv *= n
print(proizv)

# 30
import random  
def creatArray():
    r = 0
    print('Input first index matrix: ')
    x = int(input())
    print('Input second index matrix: ')
    y = int(input())
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(-100,100))
            r += 1  
    return array
D=creatArray()
proizv=1
for i in D:
    for n in i:
        if n < 0:
            proizv *= n
print(proizv)

#31
import random
n = 2
matrix = [[random.randint(-99, 99) for j in range(n)] for i in range(n)]
a=[]
for i in matrix:
    for n in i:
        a.append(n)
print(matrix)
print(min(a))


