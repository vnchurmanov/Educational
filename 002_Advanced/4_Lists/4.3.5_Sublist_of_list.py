text = input().split()


# Из входной строки текста формируется список.
# Программа выводит список, содержащий все возможные подсписки списка, включая пустой список

def chunked(some_text, num):
    result = []
    for index in range(0, len(some_text)):
        if len(some_text[index:num + index]) == num:
            result.append(some_text[index:num + index])
        else:
            break
    return result


res = [[]]
step = 1

for chunk in range(1, len(text) + 1):
    res.extend(chunked(text, chunk))
    step += 1

print(res)
