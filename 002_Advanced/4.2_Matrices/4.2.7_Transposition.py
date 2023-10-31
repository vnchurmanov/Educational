# программа транспонирует квадратную матрицу
# n — количество строк и столбцов в матрице

n = int(input())

matrix = [[int(_) for _ in input().split()] for i in range(n)]
res = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        res[j][i] = matrix[i][j]

for row in res:
    print(*row)
