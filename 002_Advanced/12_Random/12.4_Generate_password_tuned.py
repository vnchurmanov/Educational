# Те же условия, что и в п.12.3, но дополнительное условие:
# в каждом пароле обязательно должна присутствовать хотя бы одна цифра
# и как минимум по одной букве в верхнем и нижнем регистре
import random
import string


def generate_password(length):
    manifold = [_ for _ in string.ascii_letters + string.digits if _ not in "lI1oO0"]
    return "".join(random.sample(manifold, length))


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


result = []

n, m = int(input()), int(input())

while len(result) != n:
    password = generate_password(m)
    if set(password) & set(string.ascii_lowercase) and set(password) & set(string.ascii_uppercase) and set(password) & set(string.digits):
        result.append(password)


print(*result, sep="\n")
