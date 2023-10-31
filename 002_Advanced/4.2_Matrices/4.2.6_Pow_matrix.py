# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице,
# затем элементы матрицы, затем натуральное число m.
# Программа возводит квадратную матрицу в m-ую степень

n = int(input())
matrix_A = [[int(_) for _ in input().split()] for i in range(n)]
matrix_B = matrix_A.copy()
power = int(input())
enough = 1
matrix_power = [[0] * n for _ in range(n)]

while enough != power:
    for i in range(n):
        for j in range(n):
            for q in range(n):
                matrix_power[i][j] += matrix_A[i][q] * matrix_B[q][j]
    enough += 1
    matrix_B = matrix_power.copy()
    matrix_power = [[0] * n for _ in range(n)]

for row in matrix_B:
    print(*row)
