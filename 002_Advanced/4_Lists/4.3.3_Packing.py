some_text = input().split()
result = []

# вход программы - строка текста, содержащая символы.
# Программа упаковывает последовательности одинаковых символов заданной строки в подсписки
for letter in some_text:
    if result and letter == result[-1][0]:
        result[-1].append(letter)
    else:
        result.append([letter])
print(result)
