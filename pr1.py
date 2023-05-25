print("Задание 3")
import csv
import datetime
import time
with open('rows_300.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(['#', 'second', 'milisecond'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().microsecond])
        time.sleep(0.01)
        
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
