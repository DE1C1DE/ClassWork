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

