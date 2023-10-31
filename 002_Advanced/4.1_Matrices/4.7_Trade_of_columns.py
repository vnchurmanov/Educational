# На вход программе на разных строках подаются два натуральных числа n и m — количество строк и столбцов в матрице,
# затем элементы матрицы построчно через пробел, затем числа i и j — номера столбцов, подлежащих обмену

i, j = (int(input()) for _ in range(2))

matrix = [[0]*j for _ in range(i)]

for row in range(i):
    r = [int(i) for i in input().split()]
    matrix[row] = r

swap_1, swap_2 = (int(_) for _ in input().split())

for row in range(i):
    matrix[row][swap_1], matrix[row][swap_2] = matrix[row][swap_2], matrix[row][swap_1]

for row in range(i):
    for cols in range(j):
        print(str(matrix[row][cols]).ljust(3), end='')
    print()
    