# программа находит индексы (строку и столбец) первого вхождения максимального элемента

i, j = (int(input()) for _ in range(2))

matrix = [[0]*j for _ in range(i)]

for row in range(i):
    r = [int(i) for i in input().split()]
    matrix[row] = r

res = [0, 0]
max_elem = matrix[0][0]

for row in range(i):
    for cols in range(j):
        if matrix[row][cols] > max_elem:
            res[0], res[1] = row, cols
            max_elem = matrix[row][cols]
print(*res)