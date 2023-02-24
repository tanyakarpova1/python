print("Задание 1")
from random import randint
a = []
b = 10
count = 0
for c in range (b):
    a.append(randint(-100, 100))
print("Последовательность")
print(a)
for i in range(len(a) - 1):
    if (a[i] > 0 and a[i + 1] < 0) or (a[i] < 0 and a[i + 1] > 0):
        count += 1
print(count)

print ("Задание 3")
a1 = []
b1 = 10
for c1 in range (b1):
    a1.append(randint(-10, 10))
print("Последовательность")
print(a1)
if len(set(a1)) == len(a1):
    print("Все элементы уникальны")
else:
    print("Есть одинаковые элементы")

print("Задание 2")
from random import randint
a1 = []
b1 = 10
neotr = 0
otr = 0
sum1 = 0
sum2 = 0
for c1 in range (b1):
    a1.append(randint(-999, 1000))
print("Последовательность")
print(a1)
for i1 in range(len(a1)):
    if a1[i1] > 0:
        neotr = neotr + 1
        sum1 = sum1 + a1[i1]
    if a1[i1] < 0:
        otr = otr + 1
        sum2 = sum2 + a1[i1]
k1 = sum1 / neotr
k2 = sum2 / otr
print(k1)
print(k2)

