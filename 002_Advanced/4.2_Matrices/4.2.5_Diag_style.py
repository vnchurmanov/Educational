# На вход программе подаются два натуральных числа n и m.
# Программа создает матрицу размером n×m, заполняя её "диагоналями"

n, m = [int(_) for _ in input().split()]

matrix = [[0] * m for _ in range(n)]
step = 0

for q in range(n * m):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                step += 1
                matrix[i][j] = step

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
