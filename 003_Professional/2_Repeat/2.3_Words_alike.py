# Программа находит все схожие слова для заданного слова.
# Слова называются схожими, если имеют одинаковое количество и расположение гласных букв.
# При этом сами гласные могут различаться.
# После последней гласной в начальном и проверяемом слове может быть любое количество согласных.
vocals = "ауоыиэяюёе"
word = "".join(list(map(lambda x: "1" if x in vocals else "0", input())))

for _ in range(int(input())):
    check = input()
    zero_one = "".join(list(map(lambda x: "1" if x in vocals else "0", check)))
    if zero_one.rstrip("0") == word.rstrip("0"):
        print(check)

