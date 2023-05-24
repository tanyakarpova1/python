print("Задание 2")
import os
def longest_words(file):
    with open(file, "r") as text:
        words = text.read().split()
    max_length = len(max(words, key=len))
    sought_words = [word for word in words if len(word) == max_length]
    f = "result.txt"
    i = 1
    while os.path.exists(f):
        f = f"result{i}.txt"
        i += 1
    with open(f, 'w') as file:
        file.write(''.join(sought_words) + "\n")
longest_words('article.txt')

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
