#34
import random  
Result=0
a=[]
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
result=[]
for i in matrix:
    for e in i:
        if e < 0:
            Result += 1 
    a.append(Result)
    Result=0
            
print(a)
