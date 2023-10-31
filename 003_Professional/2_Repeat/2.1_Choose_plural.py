# функция choose_plural() принимает два аргумента в следующем порядке:
# amount — натуральное число, количество;
# declensions — кортеж из трех вариантов склонения существительного.

def choose_plural(amount, declens_tuple):
    ending_vars = {(0,): 2, (1,): 0, (2, 3, 4): 1, (_ for _ in range(5, 21)): 2}
    end_digit = amount
    if len(str(end_digit)) >= 2:
        if 10 <= int(str(amount)[-2:]) <= 20:
            end_digit = int(str(amount)[-2:])
        else:
            end_digit = int(str(amount)[-1])
    index_of_end = [value for key, value in ending_vars.items() if end_digit in key]
    return f"{amount} {declens_tuple[index_of_end[0]]}"


