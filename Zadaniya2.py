print ("Задание 1")
from random import randint
spisok1 = [randint(1,100) for i in range(15)]
print(spisok1)
spisok2 = [randint(1,100) for i in range(15)]
print(spisok2)
for a in spisok1:
    if a % 2 == 1:
        print("Нечетные числа: ")
        print(a)
for b in spisok2:
    if b % 2 == 0:
        print("Четные числа: ")
        print(b)

print("Задание 2")
for a in range(1,11):
    print(''.join(str(a*b) for b in range(1,11)))

print("Задание 4")
with open("Z:/text1.txt", "r") as f:
    text = f.readline(4)
    print(text)

print("Задание 5")
a = int(input('Введите число = '))
summ = 0
for i in range(1,a+1):
    summ =i+summ
print('Сумма чисел от 1')
print(summ)

print("Задание 6")
b = ["1", "2", "3", "4", "5"]
print(b)
for spisok3 in b[::-1]:
    print(spisok3)








