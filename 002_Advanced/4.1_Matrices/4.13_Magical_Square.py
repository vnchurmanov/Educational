# Магическим квадратом порядка nn называется квадратная таблица размера n×n,
# составленная из всех чисел 1, 2, 3, ..., n ** 2 (то есть все числа разные) так,
# что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой.
# Программа проверяет, является ли заданная квадратная матрица магическим квадратом

dimension = int(input())

square = [[0] * dimension for _ in range(dimension)]

for row in range(dimension):
    square[row] = [int(_) for _ in input().split()]

is_magic = sum(square[0])
flag = True
square_cols = [[0] * dimension for _ in range(dimension)]

for row in range(dimension):
    for cols in range(dimension):
        square_cols[row][cols] = square[cols][row]

for row in range(dimension):
    if sum(square[row]) != is_magic:
        flag = False
        break
    if sum(square_cols[row]) != is_magic:
        flag = False
        break
main_dia = sum(square[i][i] for i in range(dimension))
slave_dia = sum(square[i][dimension - i - 1] for i in range(dimension))

if main_dia != is_magic or slave_dia != is_magic:
    flag = False

natural_num = [int(i) for i in range(1, (dimension ** 2) + 1)]

m = []

for t in range(dimension):
    m.extend(square[t])
m.sort()

if natural_num != m:
    flag = False

print("YES" if flag else "NO")