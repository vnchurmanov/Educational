# Функция возвращает количество воскресений в году year

from datetime import date, timedelta


def num_of_sundays(year):
    my_date = date(year, 1, 1)
    checked_date = date(year + 1, 1, 1) - my_date
    week = timedelta(weeks=1)
    sundays = checked_date // week
    remain_d = (checked_date % week).days
    is_any_sundays = list(filter(lambda x: x.weekday() == 6, [date(year, 1, d) for d in range(1, remain_d + 1)]))
    return sundays if not is_any_sundays else sundays + 1

