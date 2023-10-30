i, j = (int(input()) for _ in range(2))

matrix = [[0]*j for _ in range(i)]

for n in range(i):
    for m in range(j):
        matrix[n][m] = input()

for row in range(i):
    for cols in range(j):
        print(matrix[row][cols], end=" ")
    print()

