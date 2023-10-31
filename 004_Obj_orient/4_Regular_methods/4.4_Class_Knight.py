# класс, описывающий шахматного коня
class Knight:
    def __init__(self, horizontal, vertical, color):
        self.hor_to_digit = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
                             "f": 6, "g": 7, "h": 8}
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

# метод, возвращающий символ N
    def get_char(self):
        return chr(78)

# метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по вертикальной осям
# и возвращающий True, если конь может переместиться на клетку с данными координатами
    def can_move(self, col, line):
        if abs(self.hor_to_digit[self.horizontal] - self.hor_to_digit[col]) ** 2 + \
                (self.vertical - line) ** 2 == 5:
            return True
        return False

# метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по вертикальной осям
# и заменяющий текущие координаты коня на переданные.
# Если конь из текущей клетки не может переместиться на клетку с указанными координатами,
# его координаты остаются неизменными
    def move_to(self, col, line):
        if self.can_move(col, line):
            self.horizontal = col
            self.vertical = line

# метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на которые может переместиться конь
    def draw_board(self):
        x, y = self.hor_to_digit[self.horizontal] - 1, 8 - self.vertical
        board = [['.'] * 8 for _ in range(8)]
        board[y][x] = 'N'
        for i in range(8):
            for j in range(8):
                if abs(y - i) * abs(x - j) == 2:
                    board[i][j] = '*'
        for row in board:
            print(*row, sep="")
