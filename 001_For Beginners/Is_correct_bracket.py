# функция принимает в качестве аргумента непустую строку text,
# состоящую из символов ( и ) и возвращает значение True,
# если поступившая на вход строка является правильной скобочной последовательностью
def is_correct_bracket(text):
    left = [_ for _ in text if _ == ")"]
    right = [_ for _ in text if _ == "("]
    result = [_ for _ in text]
    for s in text:
        if s == "(":
            result.pop(0)
            for m, j in enumerate(result):
                if j == ")":
                    result.pop(m)
                    break
    return not result if len(left) == len(right) else False


# Более простое решение:
# def is_correct_bracket(text):
#   while "()" in text:
#      text = text.replace("()", "")
#  return text == ""

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
