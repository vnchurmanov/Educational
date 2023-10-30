# На вход программе подаются два натуральных числа n и m -
# количество строк и столбцов в матрице.
# Программа создает матрицу размером n x m
# и заполняется таблицей умножения по формуле mult[i][j] = i * j.

i, j = (int(input()) for _ in range(2))

matrix = [[0]*j for _ in range(i)]

for row in range(i):
    for cols in range(j):
        matrix[row][cols] = row * cols
        print(str(matrix[row][cols]).ljust(3), end='')
    print()