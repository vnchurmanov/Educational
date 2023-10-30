english = "abcdefghijklmnopqrstuvwxyz"
capital_english = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def english_encrypt(text):
    result = ""
    shift = 0
    for symbol in text:
        if symbol.isalpha():
            shift += 1
    for i in text:
        if i in english:
            new_symbol = english[(english.index(i) + shift) % 26]
            result += new_symbol
        elif i in capital_english:
            new_symbol = capital_english[(capital_english.index(i) + shift) % 26]
            result += new_symbol
        else:
            result += i
    return result


txt = input().split()

for word in txt:
    print(english_encrypt(word), end=" ")

