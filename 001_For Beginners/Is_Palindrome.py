# функция принимает в качестве аргумента строку text
# и возвращает значение True, если указанный текст является палиндромом
def is_palindrome(text):
    vowels = [v for v in text.lower() if v.isalpha()]
    return vowels == vowels[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
