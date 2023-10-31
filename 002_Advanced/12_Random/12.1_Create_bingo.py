# Для игры в бинго требуется карточка размером 5×5, содержащая
# различные (уникальные) целые числа от 1 до 75 (включительно),
# при этом центральная клетка является пустой (она заполняется числом 0).
# Программа с помощью модуля random генерирует и выводит случайную карточку для игры в бинго.

import random

card = set()
while len(card) < 26:
    card.add(random.randint(1, 75))

numbers = [i for i in card]
random.shuffle(numbers)

result = [[0] * 5 for n in range(5)]

for row in range(5):
    for column in range(5):
        result[row][column] = numbers[0]
        del numbers[0]
        if row == 2 and column == 2:
            result[row][column] = 0

for r in range(5):
    for c in range(5):
        print(str(result[r][c]).ljust(3), end='')
    print()
