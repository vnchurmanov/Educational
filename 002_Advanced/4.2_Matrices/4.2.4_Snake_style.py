# На вход программе подаются два натуральных числа n и m.
# Программа создает матрицу размером n×m, заполняя её "змейкой"

n, m = [int(_) for _ in input().split()]

matrix = [[0] * m for _ in range(n)]
step = 1
for row in range(n):
    for cols in range(m):
        matrix[row][cols] = step
        step += 1

for i in range(1, n, 2):
    matrix[i].reverse()

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
