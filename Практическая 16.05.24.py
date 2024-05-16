# Задание 1
result=[]
def upper(t):
    for i in t:
        if i.isupper() == True:
            result.append(i)
    print(result)
upper("PriVet")
# Задание 2:
result=int()
Str="wdUHU..HUiwd!jjijwidjIJIWJIjds(aw!!e"
def punct(str):
    if "!" or '?' or'.' or '(' or ')' in str:
        result = str.count("!")
        result += str.count(".")
        result += str.count("?")
        result += str.count("(")
        result += str.count(")")
        print(result)
punct(Str)
#Задание 3
x=3
y=3
def create_cube(x,y):
    count = 0
    while count != y:
        print(x*"*")
        count+=1
create_cube(x,y)
#Задание 7:
def custom_filter(array):
    a=[]
    for i in array:
        if type(i) == int and i%7==0:
            a.append(i)
    if sum(a) > 83:
        return False
    else:
        return True
print(custom_filter([7, 10.5, 'txt', 14, 2, 56]))
#Задание 8:
