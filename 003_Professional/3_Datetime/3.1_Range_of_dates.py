# функция get_date_range() принимает два аргумента в следующем порядке:
# start — начальная дата, тип date
# end — конечная дата, тип date
# и возвращает список, состоящий из дат (тип date) от start до end включительно.
# Если start > end, функция возвращает пустой список

from datetime import date


def get_date_range(start, end):
    if start > end:
        return []
    return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]
