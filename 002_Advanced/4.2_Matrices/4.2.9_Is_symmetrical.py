# программа проверки симметричности квадратной матрицы относительно побочной диагонали

n = int(input())

matrix = [[int(_) for _ in input().split()] for i in range(n)]
flag = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n-j-1][n-i-1]:
            flag = False
            break

print("YES" if flag else "NO")
