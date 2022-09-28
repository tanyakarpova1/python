print ("Калькулятор");
number1 = int(input('Введите первое число: '));
number2 = int(input('Введите второе число: '));
result = input('Выберите действие: +, -, /, * ' );
#Действие сложения
if result =='+':
   print (number1+number2);
#Действие вычитания
elif result =='-':
    print (number1-number2)
#Действие умножения
elif result =='*':
   print (number1*number2)
#Действие деления
elif result =='/':
    print(number1 / number2)

print('Решение квадратного уравнения')
print('ax^2+bx+c')
a = int(input('Введите первый коэффициент: '))
b = int(input('Введите второй коэффициент: '))
c = int(input('Введите третий коэффициент: '))
print('Находим дискриминант:')
D = b**2-4*a*c
print(D);
if D < 0:
    print('Корней нет')
elif D ==0:
    x = (-b)/(2*a)
    print('Уравнение имеет один корень:')
    print(x)
elif D > 0:
    x1 = (-b+D**0.5)/(2*a)
    x2 = (-b-D**0.5)/(2*a)
    print('Уравнение имеет два корня:')
    print (x1, x2)





