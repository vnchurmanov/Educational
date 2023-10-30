import random


def is_valid(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def equal_or_not(question, guessed):
    if question > guessed:
        print("Слишком много, попробуйте еще раз")
    elif question < guessed:
        print("Слишком мало, попробуйте еще раз")
    else:
        print("Вы угадали")
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        return True


guessed_number = random.sample(range(1010), 1)
print(guessed_number)
print("Добро пожаловать в числовую угадайку")
flag = 1
tries = 0
while flag:
    tries += 1
    question = input()
    if is_valid(question):
        if equal_or_not(int(question), guessed_number[0]):
            flag = 0
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
print("Количество попыток = ", tries)
