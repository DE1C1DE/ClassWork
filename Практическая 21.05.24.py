def sum1(start, end):
    if start >end:
        start, end = end, start
    result = int()
    for i in range(start, end + 1):
        result += i
    print(result)
sum1(2, 8)
