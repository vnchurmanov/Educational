# программа поворачивает квадратную матрицу чисел на 90 град по часовой стрелке

n = int(input())

matrix = [input().split() for _ in range(n)]

res = [[0] * n for _ in range(n)]
counter = n - 1

for row in range(n):
    for col in range(n):
        res[col][counter] = matrix[row][col]
    counter -= 1

for row in res:
    print(*row)
