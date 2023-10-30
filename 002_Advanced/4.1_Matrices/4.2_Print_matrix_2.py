# программа считывает элементы матрицы один за другим,
# выводит их в виде матрицы, выводит пустую строку,
# и снова ту же матрицу, но уже поменяв местами
# строки со столбцами: первая строка выводится как первый столбец, и так далее.

i, j = (int(input()) for _ in range(2))

matrix = [[0]*j for _ in range(i)]

for n in range(i):
    for m in range(j):
        matrix[n][m] = input()

for row in range(i):
    for cols in range(j):
        print(matrix[row][cols], end=" ")
    print()

print()
for cols in range(j):
    for row in range(i):
        print(matrix[row][cols], end=" ")
    print()