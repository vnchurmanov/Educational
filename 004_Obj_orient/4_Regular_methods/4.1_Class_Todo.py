# Класс, описывающий список дел
class Todo:
    def __init__(self):
        # атрибут, хранящий список дел
        self.things = []

# метод, принимающий название дела и его приоритет (целое число) и добавляющий данное дело в список дел в виде кортежа
    def add(self, name, priority):
        self.things.append((name, priority))

# метод, принимающий в качестве аргумента целое число n и возвращающий список названий дел, имеющих приоритет n
    def get_by_priority(self, get_prior):
        return [name for name, prior in self.things if prior == get_prior]

# метод, возвращающий список названий дел, имеющих самый низкий приоритет
    def get_low_priority(self):
        priority = min(list(map(lambda x: x[1], self.things))) if self.things else None
        return self.get_by_priority(priority)

# метод, возвращающий список названий дел, имеющих самый высокий приоритет
    def get_high_priority(self):
        priority = max(list(map(lambda x: x[1], self.things))) if self.things else None
        return self.get_by_priority(priority)