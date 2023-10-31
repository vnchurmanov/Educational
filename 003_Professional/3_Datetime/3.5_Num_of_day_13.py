# Программа вычисляет, сколько тринадцатых чисел приходится на каждый день недели в период с 01.01.0001 по 31.12.9999

from datetime import date, timedelta

num_of_13 = [0 * n for n in range(7)]
counter = 1
while counter != 10000:
    start = date(counter, 1, 13)
    for i in range(1, 13):
        what_day = (date(start.year, i, 13)).weekday()
        num_of_13[what_day] += 1
    counter += 1
print(*num_of_13, sep="\n")
