# На вход программе подается строка текста.
# Программа выводит слово, которое встречается реже всего, без учета регистра.
# Если таких слов несколько, выводится то, которое меньше в лексикографическом порядке

just_words = [i.lower().strip(".,!?:;-") for i in input().split()]

result = {}
min_words = []
for word in just_words:
    result[word] = result.get(word, 0) + 1

minimum = min(result.values())
for key, value in result.items():
    if result[key] == minimum:
        min_words.append(key)
min_words.sort()
print(min_words[0])

