# функция csv_columns() принимает один аргумент:
# filename — название csv файла,
# и возвращает словарь, в котором ключом является название столбца файла filename,
# а значением — список элементов этого столбца
import csv


def csv_columns(fname) -> dict:
    with open(fname, "r", encoding="UTF-8", newline="") as f:
        keys = list(map(str.strip, f.readline().split(",")))
        writer = csv.reader(f)
        dict_res = dict()
        for line in writer:
            for i in range(len(keys)):
                dict_res[keys[i]] = dict_res.get(keys[i], []) + [line[i]]
    return dict_res
