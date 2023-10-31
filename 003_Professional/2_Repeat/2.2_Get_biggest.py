# функция get_biggest() принимает один аргумент:
# numbers — список целых неотрицательных чисел.
# Функция возвращает наибольшее число, которое можно составить из чисел из списка numbers.
# Если список numbers пуст, функция вернет число -1.

def get_biggest(num):
    return int("".join([str(_) for _ in sorted(num, key=lambda x: str(x) * len(str(max(num))), reverse=True)])) \
        if num else -1
