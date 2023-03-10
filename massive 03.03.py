print("Задание 1")
n = int(input())
a = []
for m in range(n):
    a.append([0]*n)
for m in range(n):
    for q in range(n):
        if m + q == n - 1:
            a[m][q] = 1
        elif m + q > n - 1:
            a[m][q] = 2
for row in a:
    for elem in row:
        print(elem, end = ' ')
    print()

print("Задание 2")
n1 = int(input("Введите нечетное число: "))
a1 = []
for m1 in range(n1):
    a1.append(['.']*n1)
for m1 in range(n1):
    for q1 in range(n1):
        if m1 + q1 == n1 - 1:
            a1[m1][q1] = '*'
        elif m1 == q1:
            a1[m1][q1] = '*'
        elif m1 == n1 // 2:
            a1[m1][q1] = '*'
        elif q1 == n1 // 2:
            a1[m1][q1] = '*'
for row in a1:
    for elem in row:
        print(elem, end = ' ')
    print()

print("Задание 3")
n2 = int(input())
a2 = []
for m2 in range(n):
    a2.append([1]*n2)
for m2 in range(n2):
    for q2 in range(n2):
        if m2 == q2:
            a2[m2][q2] = 0
        elif m2 > q2:
            a2[m2][q2] = m2 - q2
        elif q2 > m2:
            a2[m2][q2] = q2 - m2
for row in a2:
    for elem in row:
        print(elem, end = ' ')
    print()
