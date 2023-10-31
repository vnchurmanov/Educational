# текстовый файл files.txt содержит информацию о файлах.
# Каждая строка файла содержит три значения, разделенные символом пробела:
# имя файла, его размер (целое число) и единицы измерения.
# Программа группирует данные файлы по расширению,
# определяя общий объем файлов каждой группы, и выводит полученные группы файлов,
# указывая для каждой ее общий объем

dict1 = {}

with open("files.txt", "r", encoding="UTF-8") as file:
    all_files = [i.split() for i in file.readlines()]
    for line in all_files:
        extension = line[0].split(".")
        dict1[extension[1]] = dict1.get(extension[1], []) + [extension[0] + " " + line[1] + " " + line[2]]

bytes = {"B": 1, "KB": 1024, "MB": 1048576, "GB": 1073741824}
for key, value in sorted(dict1.items()):
    sum_bytes = 0
    what_scale = "B"
    for i in sorted(value):
        name, digit, scale = i.split()
        sum_bytes += bytes[scale] * int(digit)
        print(f"{name}.{key}")
    if sum_bytes >= bytes["GB"]:
        sum_bytes = round(sum_bytes / bytes["GB"])
        what_scale = "GB"
    elif sum_bytes >= bytes["MB"]:
        sum_bytes = round(sum_bytes / bytes["MB"])
        what_scale = "MB"
    elif sum_bytes >= bytes["KB"]:
        sum_bytes = sum_bytes // bytes["KB"]
        what_scale = "KB"
    print("-" * 10, f"Summary: {sum_bytes} {what_scale}", sep="\n")
    sum_bytes = 0
    print()
