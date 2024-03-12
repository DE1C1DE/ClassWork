#Задание 1
file = open("S:\\Группы\\ИБС215 Алгоритмизация\\Илюшин\\output.txt", "w")
file.write("conten")
# Задание 2
file=open("S:\\Группы\\ИБС215 Алгоритмизация\\Илюшин\\input.txt")
content=file.read()
file.close()
file = open("S:\\Группы\\ИБС215 Алгоритмизация\\Илюшин\\output.txt", "a")
file.write(content)
file.write("<copy>")
file.close()

# Задание 3
from datetime import datetime
file = open("S:\\Группы\\ИБС215 Алгоритмизация\\Илюшин\\logs.txt", "x")
def a(text):
    file = open("S:\\Группы\\ИБС215 Алгоритмизация\\Илюшин\\logs.txt", "a")
    date=str(datetime.now())
    file.write(date)
    file.write(text)

while True:
    a(input())
  # Задание 4
  
