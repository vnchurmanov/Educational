# функция get_all_mondays() принимает один аргумент:
# year — натуральное число
# и возвращает отсортированный по возрастанию список всех дат (тип date) года year, выпадающих на понедельник

import calendar
from datetime import datetime, timedelta


def get_all_mondays(year):
    res = []
    start = 0
    stop = datetime(year, 12, 31)
    for i in range(1, 31):
        if calendar.weekday(year, 1, i) == calendar.MONDAY:
            start = datetime(year, 1, i)
            break
    while start <= stop:
        res.append(start.date())
        start += timedelta(weeks=1)
    return res
