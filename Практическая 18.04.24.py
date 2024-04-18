№35
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
            array[i].append(random.randint(-10,10))
    return array
matrix=creatArray()
result=[]
a=int()
for i in matrix:
    for e in i:
        if e>0:
            a+=e
    result.append(a)
    a=0
print(matrix)
print(result)
№36
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
            array[i].append(random.randint(-10,10))
    return array
matrix=creatArray()
result=[]
a=[]
b=0
for i in range(y):
    for e in range(x):
        r = matrix[e][b]
        a.append(r)
    average = sum(a) / len(a)
    result.append(average)
    average=0
    a = []
    b+=1
print(matrix)
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
            array[i].append(random.randint(-10,10))
    return array
matrix=creatArray()
result=[]
c=1
a=[]
b=0
for i in range(y):
    for e in range(x):
        r = matrix[e][b]
        if r<0:
            c*=r
    a.append(c)
    c=1
    b+=1
print(matrix)
print(a)
#37
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
            array[i].append(random.randint(-10,10))
    return array
matrix=creatArray()
result=[]
c=1
a=[]
b=0
for i in range(y):
    for e in range(x):
        r = matrix[e][b]
        if r<0:
            c*=r
    a.append(c)
    c=1
    b+=1
print(matrix)
print(a)
#39
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
            array[i].append(random.randint(-10,10))
    return array
matrix=creatArray()
result=[]
a=[]
for i in matrix:
    for e in i:
        a.append(e)
    result.append(min(a))
    a=[]
print(matrix)
print(result)
#40
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
            array[i].append(random.randint(-10,10))
    return array
matrix=creatArray()
result=[]
a=0
for i in matrix:
    for e in i:
        if e!=0:
            a+=1
    result.append(a)
    a=0
print(matrix)
print(result)

