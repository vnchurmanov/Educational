# функция принимает в качестве аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр»
def convert_to_python_case(text):
    z = list(text)
    for i, s in enumerate(z[1:]):
        if s.isupper():
            z.pop(i + 1)
            z.insert(i + 1, f"_{s.lower()}")
    return z[0].lower() + "".join(z[1:])

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
