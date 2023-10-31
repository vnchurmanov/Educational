# Программа принимает на вход текущие дату и время и определяет, сколько времени осталось до релиза фичи

from datetime import datetime, timedelta

pattern = "%d.%m.%Y %H:%M"


def choose_plural(amount, variants):
    variant = 2
    if amount % 10 == 1 and amount % 100 != 11:
        variant = 0
    elif 2 <= amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
        variant = 1
    return '{} {}'.format(amount, variants[variant])


current_datetime = datetime.strptime(input(), pattern)
release = datetime.strptime("08.11.2022 12:00", pattern)
last_time_seconds = (release - current_datetime).total_seconds()
last_time_days = int(last_time_seconds / 86400)
last_time_hours = int((last_time_seconds / 3600) - (last_time_days * 24))
last_time_minutes = int((last_time_seconds / 60) - (last_time_days * 24 * 60) - (last_time_hours * 60))
days = ("день", "дня", "дней")
hours = ("час", "часа", "часов")
minutes = ("минута", "минуты", "минут")

if last_time_days >= 1:
    print(f"До релиза осталось: {choose_plural(last_time_days, days)} и "
          f"{choose_plural(last_time_hours, hours)}" if last_time_hours else
          f"До релиза осталось: {choose_plural(last_time_days, days)}")
elif last_time_hours >= 1:
    print(f"До релиза осталось: {choose_plural(last_time_hours, hours)} и "
          f"{choose_plural(last_time_minutes, minutes)}" if last_time_minutes else
          f"До релиза осталось: {choose_plural(last_time_hours, hours)}")
elif last_time_minutes >= 1:
    print(f"До релиза осталось: {choose_plural(last_time_minutes, minutes)}")
elif current_datetime >= release:
    print("Уже в проде!")
