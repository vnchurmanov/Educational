# объявление функции:
# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника
def draw_triangle(fill, base):
    middle = (base + 1) // 2
    for i in range(1, base + 1):
        if i <= middle:
            print(fill * i)
        else:
            middle -= 1
            print(fill * middle)


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)