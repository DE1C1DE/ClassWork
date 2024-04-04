#36
import random
print('Input first index matrix: ')
x = int(input())
print('Input second index matrix: ')
y = int(input())
def creatArray():
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(-100,100))
    return array
matrix=creatArray()
a=[]
b=0
result=[]
print(matrix)
for i in range(y):
    for e in range(x):
        r = matrix[e][b]
        a.append(r)
    average = sum(a)/len(a)
    result.append(average)
    average=[]
    b+=1
print(result)
#38
import random
print('Input first index matrix: ')
x = int(input())
print('Input second index matrix: ')
y = int(input())
def creatArray():
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(-100,100))
    return array
matrix=creatArray()
a=[]
b=0
result=1
print(matrix)
for i in range(y):
    for e in range(x):
        r = matrix[e][b]
        if r < 0:
            result*=r
    a.append(result)
    result=1
    b+=1
print(a)

#43
import random
print('Input first index matrix: ')
x = int(input())
print('Input second index matrix: ')
y = int(input())
def creatArray():
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(-3,3))
    return array
matrix=creatArray()
r1=[]
r2=[]
b=0
result=1
print(matrix)
l1=0
l2=0
for f in matrix:
    for p in f:
        if p==0:
            l1+=1
    r1.append(l1)
for i in range(y):
    for e in range(x):
        r = matrix[e][b]
        if r !=0:
            l2+=1
    r2.append(l2)
    b+=1
print("Нулевые элементы строки: ", r1,"Ненулевые элементы столбца: ", r2)
