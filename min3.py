x1 = int(input('Введите первое число: '));
x2 = int(input('Введите второе число: '));
x3 = int(input('Введите третье число: '));
a = [x1,x2,x3]
print('Минимальное число: ')
print (min(a))

a = int(input('Введите число: '));
k = len(str(a))
print('Количество цифр в числе: ')
print (k)

b = int(input('Введите число: '));
sum = 0
for i in range (1, b + 1):
    sum = i + sum;
print('Сумма равна: ')
print (sum)

c = int(input('Введите число: '));
factorial = 1
for e in range (1, c + 1):
    factorial = e * factorial;
print('Факториал равен: ')
print (factorial)
