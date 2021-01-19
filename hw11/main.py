# Задания
# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
# 4. Написать функцию сортировки по количеству слов в поле "text"
import json
import re

def sort_by_length(object_in_list):
    return len(object_in_list["text"].split(" "))

def sort_by_name(object_in_list):
    if len(object_in_list["name"].split(' ')) == 1:
        return object_in_list["name"].split(' ')[0]
    else:
        return object_in_list["name"].split(' ')[-1]


def sort_by_death_year(object_in_list):
    #re.findall(r"[0-9]+", object_in_list["years"])
    if "BC" in object_in_list["years"]:
        return int(re.findall(r"[0-9]+", object_in_list["years"])[-1]) * -1
    else:
        return int(re.findall(r"[0-9]+", object_in_list["years"])[-1])


def read_file_json(file_name):
    with open(file_name, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data

if __name__ == "__main__":
    json_data = read_file_json("data.json")
    sorted_by_name = sorted(json_data, key=sort_by_name)
    for i in sorted_by_name:
        print(i)
    print("=========")
    sorted_by_death = sorted(json_data, key=sort_by_death_year)
    for i in sorted_by_death:
        print(i)
    print("===========================")
    sorted_by_text = sorted(json_data, key=sort_by_length)
    for i in sorted_by_text:
        print(i)
