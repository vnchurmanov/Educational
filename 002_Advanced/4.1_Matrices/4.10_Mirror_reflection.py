# программа зеркально отображает элементы квадратной матрицы относительно горизонтальной оси симметрии

n = int(input())

matrix = [input().split() for _ in range(n)]

for row in range(int(n/2)):
    matrix[row], matrix[n - row - 1] = matrix[n - row - 1], matrix[row]

for row in matrix:
    print(*row)