# Латинским квадратом порядка nn называется квадратная матрица размером n×n,
# каждая строка и каждый столбец которой содержат все числа от 1 до n.
# Программа проверяет, является ли заданная квадратная матрица латинским квадратом

n = int(input())

matrix = [[int(_) for _ in input().split()] for i in range(n)]
trans_matrix = [[0] * n for _ in range(n)]
check = [int(i) for i in range(1, n + 1)]
flag = True

for row in matrix:
    m = sorted(row)
    if check != m:
        flag = False


for i in range(n):
    for j in range(n):
        trans_matrix[j][i] = matrix[i][j]

for row in trans_matrix:
    m = sorted(row)
    if check != m:
        flag = False

print("YES" if flag else "NO")