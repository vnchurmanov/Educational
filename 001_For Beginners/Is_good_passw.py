# функция принимает в качестве аргумента строковое значение пароля password
# и возвращает значение True, если пароль является надежным
def is_password_good(password):
    flag = False if password.isdigit() else True
    if len(password) < 8:
        flag = False
    elif password.isupper() or password.islower():
        flag = False
    elif not password.isdigit():
        for i in password:
            if i.isdigit():
                flag = True
                break
            else:
                flag = False
    return flag


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
