import math

n = int(input())


# программа выводит первые nn строк треугольника Паскаля

def n_row_pascal(row):
    result = []
    for i in range(row + 1):
        elem = math.factorial(row) / (math.factorial(i) * math.factorial(row - i))
        result.append(int(elem))
    return result


for i in range(n):
    print(*n_row_pascal(i), end="\n")
