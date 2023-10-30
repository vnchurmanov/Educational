# Следом квадратной матрицы называется сумма элементов главной диагонали.
# Программа выводит след заданной квадратной матрицы

n = int(input())
matrix = [input().split() for _ in range(n)]
print(sum(int(matrix[i][i]) for i in range(n)))
