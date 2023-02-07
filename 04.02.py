print("Задание 1")
year = int(input("Введите год: "))
print("0 - до н.э")
print("1 - н.э")
era = int(input("Введите эру от 0 до 1: "))
if ((year > 45 and era == 0 )):
    print("Год не вискосный")
if (year%4 == 0 and year%100 !=0 or year%400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")

print("Задание 2")
a = int(input("Введите число от 1 до 99: "))
if(a > 99 or a < 1):
    print("Неверное число")
elif (a == 1):
    print(a)
    print("копейка")
elif (a%10 == 2 or a%10 == 3 or a%10 == 4):
    print(a)
    print("копейки")
elif (a == 12 or a == 13 or a == 14 or a == 11):
    print(a)
    print("копеек")
else:
    print(a)
    print("копеек")

print("Задание 3")
b = int(input("Введите день года:"))
if (b < 1 or b > 365):
    print("Неверное число")
elif(b == 1):
    print("Понедельник")
elif(b%7 == 1):
    print("Понедельник")
elif(b%7 == 2):
    print("Вторник")
elif(b%7 == 3):
    print("Среда")
elif(b%7 == 4):
    print("Четверг")
elif(b%7 == 5):
    print("Пятница")
elif(b%7 == 6):
    print("Суббота")
elif(b%7 == 7):
    print("Воскресенье")

print("Задание 4")
d = int(input("Введите день рождения"))
n = int(input("Введите номер месяца рождения"))
if ((d >= 21 and n == 3) or (d <= 20 and n == 4)):
    print("Знак Зодиака - Овен")
elif ((d >= 21 and n == 4) or ( d <= 20 and n == 5)):
    print("Знак Зодиака - Телец")
elif ((d >= 21 and n == 5) or ( d <= 21 and n == 6)):
    print("Знак Зодиака - Близнецы")
elif ((d >= 22 and n == 6) or ( d <= 22 and n == 7)):
    print("Знак Зодиака - Рак")
elif ((d >= 23 and n == 7) or ( d <= 23 and n == 8)):
    print("Знак Зодиака - Лев")
elif ((d >= 24 and n == 8) or ( d <= 23 and n == 9)):
    print("Знак Зодиака - Дева")
elif ((d >= 24 and n == 9) or ( d <= 23 and n == 10)):
    print("Знак Зодиака - Весы")
elif ((d >= 24 and n == 10) or ( d <= 22 and n == 11)):
    print("Знак Зодиака - Скорпион")
elif ((d >= 23 and n == 11) or ( d <= 21 and n == 12)):
    print("Знак Зодиака - Стрелец")
elif ((d >= 22 and n == 12) or ( d <= 20 and n == 1)):
    print("Знак Зодиака - Козерог")
elif ((d >= 21 and n == 1) or ( d <= 18 and n == 2)):
    print("Знак Зодиака - Водолей")
elif ((d >= 19 and n == 2) or ( d <= 20 and n == 3)):
    print("Знак Зодиака - Рыбы")


