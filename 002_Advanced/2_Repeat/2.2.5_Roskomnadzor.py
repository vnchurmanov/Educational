sentence = input() + " запретил букву "
alphabet = []
rus = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

for vowel in sentence:
    if vowel in rus:
        if vowel not in alphabet:
            alphabet.append(vowel)
alphabet.sort()

for index in range(len(alphabet)):
    print(" ".join(sentence.split()), alphabet[index], sep=" ")
    for vowel in sentence:
        if vowel == alphabet[index]:
            sentence = sentence.replace(vowel, "")

# Output:
# роскомнадзор запретил букву а
# роскомндзор зпретил букву б
# роскомндзор зпретил укву в
# роскомндзор зпретил уку д
# роскомнзор зпретил уку е
# роскомнзор зпртил уку з
# роскомнор пртил уку и
# роскомнор пртл уку к
# росомнор пртл уу л
# росомнор прт уу м
# росонор прт уу н
# росоор прт уу о
# рср прт уу п
# рср рт уу р
# с т уу с
# т уу т
# уу у