# Файл salary_data.csv содержит анонимную информацию о зарплатах сотрудников в различных компаниях.
# В первом столбце записано название компании, а во втором — зарплата очередного сотрудника.
# Программа упорядочивает компании по возрастанию средней зарплаты ее сотрудников
# и выводит их названия, каждое на отдельной строке
import csv

with open("salary_data.csv", "r", encoding="UTF-8", newline="") as file:
    all_salaries = csv.DictReader(file, delimiter=";")
    salaries_dict = dict()
    workers = dict()
    for worker in all_salaries:
        salaries_dict[worker["company_name"]] = salaries_dict.get(worker["company_name"], 0) + int(worker["salary"])
        workers[worker["company_name"]] = workers.get(worker["company_name"], 0) + 1

for company, salary in salaries_dict.items():
    salaries_dict[company] = int(salary / workers[company])

print(*[company for company, salary in sorted(salaries_dict.items(), key=lambda x: (x[1], x[0]))], sep="\n")

