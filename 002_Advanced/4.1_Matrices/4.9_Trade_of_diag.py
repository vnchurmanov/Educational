# программа меняет местами элементы, стоящие на главной и побочной диагонали квадратной матрицы,
# при этом каждый элемент не из диагонали остается в том же столбце

n = int(input())

matrix = [input().split() for _ in range(n)]

for row in range(n):
    matrix[row][row], matrix[n - row - 1][row] = matrix[n - row - 1][row], matrix[row][row]

for row in range(n):
    for cols in range(n):
        print(str(matrix[row][cols]).ljust(3), end='')
    print()