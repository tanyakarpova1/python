print(("Задание 1"))
def fun1(str):
    x = 0
    for i in str:
        x += 1
    return x
str = "word"
print(fun1(str))

print(("Задание 3"))
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2-1 and y1 == y2-1:
    print("YES")
else:
    print("NO")

print("Задание 4")
c = [1,5,7]
d = [3,2,4]
a = []
a.insert(0,c[0])
a.insert(1,d[0])
a.insert(2,c[1])
a.insert(3,d[1])
a.append(c[2])
a.append(d[2])
print(a)

print("Задание 5")
def calculation():
    q = int(input())
    w = int(input())
    print(q+w)
    print(q-w)
print(calculation())