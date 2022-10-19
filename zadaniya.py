print ('Задание 1')
print ('a)(101 + 0)/3')
a = 101
b = 0
c = 3
d = (a+b)/3
print (d)

print ('b) 3.0e-6*10000000.1')
e = 2.71
x = (3.0*e) - (6*10000000.1)
print (x)

print ('c)true&&true')
y = True and True
print (y)

print ('d)false&&false')
x1 = False and False
print(x1)

print ('e)(false&&false)(true&&true)')
x2 = False and False
x3 = True and True
x4 = x2 and x3
print (x4)

print ('f)(false false)&&(true&&true)')
x5 = False and False
x6 = True and False
x7 = x5 and x6
print (x7)

print ('Задание 2')
y1 = int(input('Введите целое число'))
y2 = int(input('Введите целое число'))
y3 = int(input('Введите целое число'))
y4 = int(input('Введите целое число'))
if y1 == y2 ==y3 ==y4:
   print('Числа равны')
else:
    print ('Числа не равны')

print ('Задание 3')
y5 = int(input('Введите целое число'))
y6 = int(input('Введите целое число'))
y7 = int(input('Введите целое число'))
y8 = int(input('Введите целое число'))
a1 = [y5,y6,y7,y8]
print ('Максимальное число:')
print (max(a1))

print ('Задание 4')
y9 = int(input('Введите целое число'))
y10 = int(input('Введите целое число'))
y11 = int(input('Введите целое число'))
y12 = int(input('Введите целое число'))
a2 = [y9,y10,y11,y12]
print ('Минимальное число:')
print (min(a2))

print ('Задание 5')
n1 = int(input('Введите целое число'))
n2 = int(input('Введите целое число'))
n3 = int(input('Введите целое число'))
n4 = int(input('Введите целое число'))
a3 = [n1,n2,n3,n4]
sr = (n1 + n2 + n3 + n4)/4
print('Среднее значение чисел массива:')
print (sr)
print ('Числа, превышающее среднее значение чисел массива: ')
if n1 > sr:
    print (n1)
if n2 > sr:
    print (n2)
if n3 > sr:
    print (n3)
if n4 > sr:
    print (n4)

print ('Задание 6')
from functools import reduce
from operator import mul
k1 = int(input('Введите целое число'))
k2 = int(input('Введите целое число'))
a4 =[k1,k2]
k3 = reduce(mul,a4)
print ('Результат умножения: ')
print (k3)

print ('Задание 9')
t1 = int(input('Введите свой рост в см: '))
t2 = int(input('Введите свой вес: '))
t1 = t1/100
imt = t2/t1**2
print ('Ваш индекс массы тела')
print (imt)
if imt <18.5:
    print ('Ваш вес ниже нормального ')
elif imt <=25:
    print ('Ваш вес в норме')
elif imt <=30:
    print ('Избыточный вес')
elif imt <=35:
    print('Ожирение первой степени')
elif imt <=40:
    print('Ожирение второй степени')
elif imt >40:
    print('Ожирение третьей степени')

print ('Задание 10')
ch = int(input('Введите число'))
kvadrat = ch*ch
kub =ch*ch*ch
chetvertaya = ch*ch*ch*ch
print('Квадрат числа: ')
print(kvadrat)
print('Куб числа: ')
print(kub)
print('Четвертая степень: ')
print(chetvertaya)

print ('Задание 11')
st1 = int(input('Введите длину первой стороны треугольника'))
st2 = int(input('Введите длину второй стороны треугольника'))
st3 = int(input('Введите длину третьей стороны треугольника'))
if st1 + st2 > st3 and st1 + st3 > st2 and st2 + st3 > st1:
    print('Данные стороны образуют треугольник')
else:
    print('Данные стороны не образуют треугольник')







