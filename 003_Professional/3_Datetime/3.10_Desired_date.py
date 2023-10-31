# Программа вычисляет каждый 3 четверг месяца
import calendar
from datetime import date


def get_all_days(year, desired_day):
    all_days = [calendar.monthrange(year, i)[1] for i in range(1, 13)]
    result = dict()
    for index, month in enumerate(all_days):
        for day in range(1, month + 1):
            if calendar.weekday(year, index + 1, day) == desired_day:
                result[index + 1] = result.get(index + 1, []) + [date(year, index + 1, day)]
    return result


all_thursdays = get_all_days(int(input()), 3)
res = [i[2] for i in all_thursdays.values()]
print(*[day.strftime("%d.%m.%Y") for day in res], sep="\n")
