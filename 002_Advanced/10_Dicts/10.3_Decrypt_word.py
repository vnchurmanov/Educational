# Программа для расшифровки секретного слова методом частотного анализа.
# В первой строке задано зашифрованное слово. Во второй строке задано одно целое число n – количество букв в словаре.
# В следующих n строках записано, сколько раз конкретная буква алфавита встречается в этом слове – <буква>: <частота>

word = input()
cypher = {}
numbers = ""
for symb in word:
    cypher[symb] = cypher.get(symb, 0) + 1
for symb in word:
    numbers += str(cypher[symb])
decrypt = {}
for _ in range(int(input())):
    letter = input().split(": ")
    decrypt[letter[1]] = decrypt.get(int(letter[1]), letter[0])
for _ in numbers:
    print(decrypt[_], end="")

