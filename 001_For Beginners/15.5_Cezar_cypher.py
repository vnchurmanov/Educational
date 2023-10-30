rus = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
english = "abcdefghijklmnopqrstuvwxyz"


#direction = int(input("Шифрование (наберите 0) или дешифрование (наберите 1)?"))
#alphabet = int(input("Русский алфавит (наберите 0) или английский (наберите 1)?"))
#shift_step = int(input("Каков шаг сдвига?"))
#text = input("Текст?")


def rus_encrypt(text, shift):
    result = ""
    for i in text.lower():
        if i in rus:
            new_symbol = rus[(rus.index(i) + shift) % 32]
            result += new_symbol
        else:
            result += i
    return result


def rus_decrypt(text, shift):
    result = ""
    for i in text.lower():
        if i in rus:
            new_symbol = rus[(rus.index(i) - shift) % 32]
            result += new_symbol
        else:
            result += i
    return result


def english_encrypt(text, shift):
    result = ""
    for i in text.lower():
        if i in english:
            new_symbol = english[(english.index(i) + shift) % 26]
            result += new_symbol
        else:
            result += i
    return result


def english_decrypt(text, shift):
    result = ""
    for i in text.lower():
        if i in english:
            new_symbol = english[(english.index(i) - shift) % 26]
            result += new_symbol
        else:
            result += i
    return result


txt = "Hawnj pk swhg xabkna ukq nqj."

for _ in range(25):
    print(english_decrypt(txt, _))

