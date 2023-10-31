# На вход программе подаются два натуральных числа n и m.
# Программа создает матрицу размером n×m и заполняет её числами от 1 до n⋅m

n, m = [int(i) for i in input().split()]
stop = 1

matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = stop
        print(str(matrix[i][j]).ljust(3), end='')
        stop += 1
    print()