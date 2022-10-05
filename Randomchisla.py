from random import randint
spisok1 = [randint(1,10000) for i in range (15)]
print ('Случайные пололожительные числа:')
print (spisok1)
print ('Сумма чисел:')
print (sum(spisok1))
spisok2 = [randint(-10000,-1) for i in range (15)]
print ('Случайные отрицательные числа:')
print (spisok2)
print ('Сумма чисел:')
print (sum(spisok2))