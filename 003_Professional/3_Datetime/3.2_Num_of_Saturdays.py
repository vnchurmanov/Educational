# Функция saturdays_between_two_dates() принимает два аргумента в следующем порядке:
# start — начальная дата, тип date
# end — конечная дата, тип date
# и возвращает количество суббот между датами start и end включительно
from datetime import date


def saturdays_between_two_dates(start, end):
    if start > end:
        start, end = end, start
    all_saturdays = [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)
                     if date.fromordinal(i).weekday() == 5]
    return len(all_saturdays)
