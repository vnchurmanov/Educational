# На вход программе подается натуральное число n.
# Программа создает матрицу размером n×n и заполняет её по следующему правилу:
# - числа на побочной диагонали равны 1;
# - числа, стоящие выше этой диагонали, равны 0;
# - числа, стоящие ниже этой диагонали, равны 2

n = int(input())

matrix = [[0] * n for _ in range(n)]

for row in range(n):
    for col in range(n):
        if col == n - row - 1:
            matrix[row][col] = 1
        elif col > n - row - 1:
            matrix[row][col] = 2

for row in matrix:
    print(*row)
