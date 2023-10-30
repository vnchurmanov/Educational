# объявление функции
def draw_triangle(amount, height):
    for i in range(amount):
        for j in range(height + 1):
            print("*" * j)


# основная программа
draw_triangle(1, 10)  # вызов функции
