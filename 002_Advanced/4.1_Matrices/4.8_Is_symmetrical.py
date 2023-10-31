# программа проверяет симметричность квадратной матрицы относительно главной диагонали

n = int(input())

matrix = [input().split() for _ in range(n)]

result = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            result = False
            break

print("YES" if result else "NO")