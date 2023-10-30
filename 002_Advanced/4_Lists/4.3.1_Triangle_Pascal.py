import math

# Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму.
# В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.
# Программа возвращает n строку треугольника Паскаля в виде списка (нумерация строк начинается с нуля)

n = int(input())
result = []
for i in range(n + 1):
    elem = math.factorial(n) / (math.factorial(i) * math.factorial(n - i))
    result.append(int(elem))
print(result)