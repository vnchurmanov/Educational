# класс, описывающий расширяемый набор слов
class Wordplay:
    def __init__(self, words=()):
        self.words = [_ for _ in words]

# метод, принимающий в качестве аргумента слово и добавляющий его в набор.
# Если слово уже есть в наборе, метод ничего не должен делать
    def add_word(self, word):
        if word not in self.words:
            self.words.append(word)

# метод, принимающий в качестве аргумента натуральное число n
# и возвращающий список слов из набора, длина которых равна n
    def words_with_length(self, n):
        return list(filter(lambda x: len(x) == n, self.words))

# метод, принимающий произвольное количество аргументов — букв,
# и возвращающий все слова из набора, которые включают в себя только переданные буквы
    def only(self, *args):
        return [word for word in self.words if set(word) == set(args) or set(word).issubset(set(args))]

# метод, принимающий произвольное количество аргументов — букв,
# и возвращающий все слова из списка words, которые не содержат ни одну из этих букв
    def avoid(self, *args):
        return [word for word in self.words if set(word).isdisjoint(set(args))]
