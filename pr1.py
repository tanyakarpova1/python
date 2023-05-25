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
