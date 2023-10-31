# Функция is_available_date() принимает два аргумента в следующем порядке:
# booked_dates — список строковых дат, недоступных для бронирования.
# Элементом списка является либо одиночная дата, либо период (две даты через дефис).
# Например: ['04.11.2021', '05.11.2021-09.11.2021']
# date_for_booking — одиночная строковая дата или период (две даты через дефис),
# на которую гость желает забронировать номер. Например:
# '01.11.2021' или '01.11.2021-04.11.2021'
# Функция is_available_date() возвращает True, если дата или период date_for_booking
# полностью доступна для бронирования. В противном случае функция возвращает False

from datetime import datetime, timedelta


def from_str_to_list(date):
    res = []
    if "-" in date:
        start, stop = [datetime.strptime(i, "%d.%m.%Y") for i in date.split("-")]
        res.append(start)
        while start != stop:
            start += timedelta(days=1)
            res.append(start)
    else:
        res.append(datetime.strptime(date, "%d.%m.%Y"))
    return res


def is_available_date(booked_dates, date_for_booking):
    already_booked = []
    for date in booked_dates:
        already_booked += from_str_to_list(date)
    desirable = from_str_to_list(date_for_booking)
    return not list(filter(lambda x: x in already_booked, desirable))
