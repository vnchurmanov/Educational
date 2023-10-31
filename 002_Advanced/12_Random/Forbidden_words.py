# На вход программе подается строка текста с именем текстового файла.
# Программа выводит на экран содержимое этого файла, но с заменой всех запрещенных слов звездочками *
# (количество звездочек равно количеству букв в слове).
# Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt.
# Гарантируется, что все слова в этом файле записаны в нижнем регистре

with open(input(), "r") as text, open("forbidden_words.txt", "r") as words:
    forbidden = list(words.read().split())
    all_words = text.read()
    text_lower = all_words.lower()
    for word in forbidden:
        text_lower = text_lower.replace(word, "*" * len(word))
print(*map(lambda x: x[0] if x[1] != "*" else x[1], zip(all_words, text_lower)), sep="")
