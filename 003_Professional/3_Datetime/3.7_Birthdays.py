# Дан список сотрудников организации, в котором указаны их фамилии, имена и даты рождения.
# Программа определяет самого молодого сотрудника,
# празднующего свой день рождения в течение ближайших семи дней от текущей даты

from datetime import datetime, timedelta

pattern = "%d.%m.%Y"
date_start = datetime.strptime(input(), pattern) + timedelta(days=1)
date_end = date_start + timedelta(days=6)
all_stuff = [input().split() for i in range(int(input()))]
dict_nearest_7 = dict()
for man in all_stuff:
    date = datetime.strptime(man[2], pattern)
    if date_start < date.replace(year=date_start.year) <= date_end or \
            date_start < date.replace(year=date_start.year + 1) <= date_end:
        dict_nearest_7[date] = dict_nearest_7.get(date, man[:2])
print(*sorted(dict_nearest_7.items(), reverse=True)[0][1] if dict_nearest_7 else ["Дни рождения не планируются"])
