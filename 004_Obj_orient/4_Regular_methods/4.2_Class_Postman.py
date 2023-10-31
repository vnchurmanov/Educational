# Класс, описывающий почтальона
class Postman:
    def __init__(self):
        self.delivery_data = []

# метод, принимающий в качестве аргументов улицу, дом и квартиру
    def add_delivery(self, street, house, flat):
        return self.delivery_data.append((street, house, flat))

#  метод, принимающий в качестве аргумента улицу и возвращающий список всех домов на этой улице,
#  в которые требуется доставить письма
    def get_houses_for_street(self, desired_street):
        return list({h: None for s, h, _ in self.delivery_data if s == desired_street})

# метод, принимающий в качестве аргументов улицу и дом
# и возвращающий список всех квартир в этом доме, в которые требуется доставить письма
    def get_flats_for_house(self, desired_street, desired_house):
        return list({f: None for s, h, f in self.delivery_data if s == desired_street and h == desired_house})
