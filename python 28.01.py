print("Задание 1")

x1 = int(input("Введите X: "))
y1 = int(input("Введите Y: "))
if ((y1 <= 1) or (y1 >= 1) and (x1 <=1 ) or (x1 >=1 )):
    print("Точка попадает в заштрихованную область")
else:
    print("Точка не попадает в заштрихованную область")

print("Задание 3a")
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = a%2
if (c==0):
    print("Число a-четное")
d = b%2
if (d==0):
    print("Число b-четное")
if ((c==0 or d==0) and c !=d):
    print("Условие истинно")
else:
    print("Условие ложно")

print("Задание 3a")
a1 = int(input("Введите a1: "))
b1 = int(input("Введите b1: "))
v1 = int(input("Введите v1: "))
c1 = a1%3
d1 = b1%3
e1 = v1%3
if (c1==0 and d1==0 and e1==0):
    print("Условие истинно")
else:
    print("Условие ложно")
    
print("Задание 2")
t = int(input("Введите время начала разговора в часах: "))
dt = int(input("Введите продолжительность разговора в минутах: "))
d = int(input("Введите день недели от 1 до 7: "))
s = int(input("Введите стоимость минуты разговора: "))
skidka = 0
skidka1 = 0
r = dt*s
print("Стоимость разговора: ")
print(r)
if (t >= 22 or t <= 8):
    skidka = r / 5
    r1 = r - skidka
    print("Общая стоимость со скидкой на время:")
    print(r1)
if (d==6 or d==7):
    skidka1 = r / 10
    r2 = r - skidka1
    print("Общая стоимость со скидкой за день недели: ")
    print(r2)
if (skidka > 0 and skidka1 > 0):
    r = r - (skidka + skidka1)
    print("Конечная стоимость: ")
    print(r)
