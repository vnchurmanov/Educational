text = input().split()
chunk = int(input())


# вход программы - две строки: на одной – символы, на другой – число nn. Из первой строки формируется список.
# Функция принимает на вход список и число, задающее размер чанка (куска),
# а возвращает список из чанков (кусков) указанной длины

def chunked(some_text, num):
    result = []
    for index in range(0, len(some_text), num):
        result.append(list(some_text[index:(num + index):]))
    return result


print(chunked(text, chunk))
