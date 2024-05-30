#Задание 1
from PIL import Image as image
image=image.open('S:\\Группы\\ИБС215 Алгоритмизация\\III Сложные задания\\Практическое задание PIL\\screenshot.JPG')
screenshot_bw = image.convert("L")
screenshot_bw.save("screenshot_bw.png")
#Задание 2
from PIL import Image as image
image=image.open('S:\\Группы\\ИБС215 Алгоритмизация\\III Сложные задания\\Практическое задание PIL\\screen_camera.PNG')
screenshot_bw = image.rotate(180)
screenshot_bw.save("screen_camera.png")
#Задание 4
from PIL import Image, ImageFont, ImageDraw
image=Image.open('S:\\Группы\\ИБС215 Алгоритмизация\\III Сложные задания\\Практическое задание PIL\\figures.png')
image = Image.new("RGB", (200, 200), "white")
draw = ImageDraw.Draw(image)
draw.rectangle((50, 50, 150, 150), outline="red", fill="blue")
font = ImageFont.truetype("arial.ttf", 10)
draw.text((60, 85), "Саня был здесь", fill="black", font=font)
image.show()
#Задание 5
