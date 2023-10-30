# На вход программе подается число nn, а затем nn строк,
# содержащих целые числа в порядке возрастания.
# Из данных строк формируются списки чисел.
# Программа объединяет указанные списки в один отсортированный список
def quick_merge(num_of_str):
    result = []
    for i in range(num_of_str):
        result += [int(d) for d in input().split()]
    return sorted(result)


print(*quick_merge(int(input())))
