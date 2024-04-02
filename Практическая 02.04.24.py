#35
import random  
Result=0
a=[]
def creatArray():
    r = 0
    x = 7
    y = 4
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(-100,100))
            r += 1  
    return array
matrix=creatArray()
print(matrix)
result=[]
for i in matrix:
    for e in i:
        if e > 0:
            Result += e 
    a.append(Result)
    Result=0
            
print(a)

#37
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
            array[i].append(random.randint(-1,1))
            r += 1  
    return array
matrix=creatArray()
print(matrix)
a=[]
for i in matrix:
    for e in i:
        if e != 0:
            a.append(e)
            
print(a)

#39
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
matrix=creatArray()
print(matrix)
a=[]
Min=int()
for i in matrix:
    Min=min(i)
    a.append(Min)
#40
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
            array[i].append(random.randint(-1,1))
            r += 1  
    return array
matrix=creatArray()
print(matrix)
a=[]
count=0
for i in matrix:
    for e in i:
        if e != 0:
            a.append(e)
print(a)
#42
import random  
print('Input first index matrix: ')
x = int(input())
print('Input second index matrix: ')
y = int(input())
def creatArray():
    r = 0
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(-10,10))
            r += 1  
    return array
matrix=creatArray()
print(matrix)
a=[]
c=[]
b=0
r=int()
for i in range(y):
    for e in range(x):
        a.append(matrix[e][b])
    r=max(a)
    c.append(r)
    r=0
    a=[]
    b+=1
print(c)
#41
import random  
print('Input first index matrix: ')
x = int(input())
print('Input second index matrix: ')
y = int(input())
def creatArray():
    r = 0
    array = []
    for i in range(x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(-10,10))
            r += 1  
    return array
matrix=creatArray()
print(matrix)
a=1
c=[]
b=0
r=1
for i in range(y):
    for e in range(x):
        r = matrix[e][b]
        if int(r) > 0:
            a*=r
    c.append(a)
    r=1
    a=1
    b+=1
print(c)

