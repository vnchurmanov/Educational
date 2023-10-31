# Программа с помощью модуля random генерирует n паролей длиной m символов,
# состоящих из строчных и прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:
# «l» (L маленькое);
# «I» (i большое);
# «1» (цифра);
# «o» и «O» (маленькая и большая буквы);
# «0» (цифра).
import random
import string


def generate_password(length):
    manifold = [_ for _ in string.ascii_letters + string.digits if _ not in "lI1oO0"]
    return "".join(random.sample(manifold, length))


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


print(*generate_passwords(int(input()), int(input())), sep="\n")
