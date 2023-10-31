# На вход программе подаются два натуральных числа n и m.
# Программа создает матрицу размером n×m, заполнив её символами . и * в шахматном порядке.
# В левом верхнем углу стоит точка

n, m = [int(i) for i in input().split()]

matrix = [["."] * m for _ in range(n)]

for row in range(n):
    for col in range(m):
        if not(row % 2) and (col % 2):
            matrix[row][col] = "*"
        elif (row % 2) and not(col % 2):
            matrix[row][col] = "*"

for row in matrix:
    print(*row)