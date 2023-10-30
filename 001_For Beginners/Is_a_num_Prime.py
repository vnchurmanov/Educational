# функция принимает в качестве аргумента натуральное число
# и возвращает значение True, если число является простым
def is_prime(num):
    flag = True if num != 1 else False
    for d in range(2, num):
        if not (num % d):
            flag = False
    return flag


# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
