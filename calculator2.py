while True:
    number1 = int(input('Введите первое число: '));
    number2 = int(input('Введите второе число: '));
    result = input('Выберите действие: +, -, /, * ');
    if result == '+':
        number3 = number1 + number2;
        print(number3)
        break
    elif result == '-':
        number3 = number1 - number2;
        print(number3)
        break
    elif result == '*':
        number3 = number1 * number2;
        print(number3)
        break
    elif result == '/':
        number3 = number1 / number2;
        print(number3)
        break
    else:
        print("Неверно выбрано действие")
        break

print('Решение квадратного уравнения')
print('ax^2+bx+c')
a = int(input('Введите первый коэффициент: '))
b = int(input('Введите второй коэффициент: '))
c = int(input('Введите третий коэффициент: '))
print('Находим дискриминант:')
D = b**2-4*a*c
if D < 0:
    print('Корней нет')
elif D ==0:
    x = (-b)/(2*a)
    print('Уравнение имеет один корень:')
    print(x)
elif D > 0:
    x1 = (-b+D**0.5)/(2*a)
    x2 = (-b-D**0.5)/(2*a)
    print('Уравнение имеет положительный дискриминант и два корня:')
    spisok = [D, x1, x2]
    print (spisok)