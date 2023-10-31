# В текстовом файле cyrillic.txt содержится текст.
# Программа для транслитерации этого файла, то есть замены кириллических символов
# на латинские. Все остальные символы оставляются без изменений.
# Результат транслитерации записывается в файл transliteration.txt

with open("cyrillic.txt", "r") as text, open("transliteration.txt", "w") as output:
    dict1 = {
        'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
        'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
        'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
        'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
    }
    result = ""
    for symb in text.read():
        if symb.lower() in dict1:
            result += dict1[symb.lower()] if symb.islower() else dict1[symb.lower()].title()
        else:
            result += symb
    print(result, file=output)

