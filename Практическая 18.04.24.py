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
