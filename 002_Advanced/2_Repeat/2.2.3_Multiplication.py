# Программа определяет, является ли число произведением двух чисел из данного набора.
# В первой строке подаётся число n (0 < n < 1000) – количество чисел в наборе.
# В последующих nn строках вводятся целые числа, составляющие набор (могут повторяться).
# Затем следует целое число, которое является или не является произведением двух каких-то чисел из набора

num_amount = int(input())
kit_of_numbers = [int(input()) for _ in range(num_amount)]
checked_num = int(input())
result = False

for index, num in enumerate(kit_of_numbers):
    for ind, sec_num in enumerate(kit_of_numbers):
        if index == ind:
            continue
        else:
            if num * sec_num == checked_num:
                result = True
                break

print("ДА" if result else "НЕТ")