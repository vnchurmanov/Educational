# Программа для подсчета количества единиц каждого вида товара из приобретенных каждым покупателем интернет-магазина.
# На вход программе подается число n — количество строк в базе данных о продажах интернет-магазина.
# Далее следует n строк с записями вида покупатель товар количество,
# где покупатель — имя покупателя (строка без пробелов), товар — название товара (строка без пробелов),
# количество — количество приобретенных единиц товара (натуральное число)

dict1 = {}

for _ in range(int(input())):
    purchase = input().split()
    if purchase[0] not in dict1.keys():
        dict1.setdefault(purchase[0], {purchase[1]: int(purchase[2])})
    else:
        dict1[purchase[0]][purchase[1]] = dict1[purchase[0]].get(purchase[1], 0) + int(purchase[2])

for keys in sorted(dict1.keys()):
    print(keys, ":", sep="")
    for key, value in sorted(dict1[keys].items()):
        print(key, value)
