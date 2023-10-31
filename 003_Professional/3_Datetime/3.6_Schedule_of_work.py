# Дан режим работы магазина (пн-пт с 9 до 21, сб-вс с 10 до 18)
# Программа принимает на вход текущие дату и время и определяет количество минут, оставшееся до закрытия магазина

from datetime import date, time, datetime, timedelta

schedule = {(0, 1, 2, 3, 4): [time(9, 0), time(21, 0)], (5, 6): [time(10, 0), time(18, 0)]}
current_datetime = datetime.strptime(input(), "%d.%m.%Y %H:%M")
what_day = current_datetime.weekday()
for key, value in schedule.items():
    if what_day in key:
        what_time = current_datetime.time()
        if value[1] > what_time >= value[0]:
            print(value[1].hour * 60 - (what_time.hour * 60 + what_time.minute))
        else:
            print("Магазин не работает")
