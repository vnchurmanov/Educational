# Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями:
# верхнюю, нижнюю, левую и правую.
# программа вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.

n = int(input())

matrix = [[0] * n for _ in range(n)]

for i in range(n):
    row = [int(_) for _ in input().split()]
    matrix[i] = row

summation = {"Верхняя четверть": 0,
             "Правая четверть": 0,
             "Нижняя четверть": 0,
             "Левая четверть": 0}

for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            summation["Верхняя четверть"] += matrix[i][j]
        elif i < j and i > n - 1 - j:
            summation["Правая четверть"] += matrix[i][j]
        elif i > j and i > n - 1 - j:
            summation["Нижняя четверть"] += matrix[i][j]
        elif i > j and i < n - 1 - j:
            summation["Левая четверть"] += matrix[i][j]

for k, v in summation.items():
    print("{0}: {1}".format(k, v))