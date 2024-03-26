# 27
a=[1, 2, 1, 2, 3, 4, 3, 2, 4, 2, 4, 6, 5, 7, 8, 9,6, 7, 8, 5, 3, 4, 5, 8, 6]
b=[2, 4, 5, 3, 2, 5, 6, 7, 8, 8, 4, 5, 6, 7, 8, 9, 2]
print(set(a+b))

#28
B=[[1, 3, 0],[1, 5, 7]]
count=0
for i in B:
    for n in i:
        if n != 0:
            count+=1
print(B)
print(count)

#29
D=[[1, -3, 0],[1, -5, 7]]
proizv=1
for i in D:
    for n in i:
        if n < 0:
            proizv *= n
print(proizv)

# 30
import random
n = 2
matrix = [[random.randint(-99, 99) for j in range(n)] for i in range(n)]
proizv=1
for i in matrix:
    for n in i:
        if n > 0:
            proizv *= n
print(matrix)
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


