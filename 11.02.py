from random import randint
a = 250
b = []
for c in range(a):
    b.append(randint(0,10000))
print("Изначальный массив")
print(b)
for c in range(a-1):
    for d in range(a-c-1):
        if b[d] > b[d+1]:
            b[d], b[d+1] = b[d+1], b[d]
print("Отсортированный массив")
print(b)