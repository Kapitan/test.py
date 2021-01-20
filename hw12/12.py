# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).
import requests
import csv
import re
import json


def get_uniq_q_in_list(count):
    url = "http://api.forismatic.com/api/1.0/"
    parametr = {
        "method": "getQuote",
        "format": "json",
        "key": 1,
        "lang": "ru"
    }
    x = []
    while len(x) < count:
        r = (requests.get(url, params=parametr)).json()
        if (r not in x) and (r["quoteAuthor"] != ''):
            x.append(r)
    return x


def write_csv_file(data, filename="text.csv"):
    data2 = sorted(data, key=sort_by_name)
    with open(filename, "w") as filecsv:
        fnames = ['quoteAuthor', 'quoteText', 'quoteLink']
        headerss = {'quoteAuthor': 'Author', 'quoteText': 'Quote', 'quoteLink': 'URL'}
        writer = csv.DictWriter(filecsv, fieldnames=fnames, extrasaction='ignore')
        writer.writerow(headerss)
        for row in data2:
            writer.writerow(row)


def sort_by_name(dict_obj):
    return dict_obj["quoteAuthor"]


write_csv_file(get_uniq_q_in_list(30))

# 2. Дан файл authors.txt
# 2.1) написать функцию, которая считывает данные из этого файла,
# возвращая СПИСОК тех строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.


def read_file_txt(filename):
    list_of = []
    reg = r"\d{1,2}[a-z]{2}\s[A-Z][a-z]{2,8}\s\d{4}"
    reg2 = r"-.+\w+\b's"
    with open(filename, "r") as filetxt:
        for strings1 in filetxt.readlines():
            if (("birthday" in strings1.lower()) or ("death" in strings1.lower())) and re.findall(reg, strings1) and re.findall(reg2, strings1):
                list_of.append(strings1)
    return list_of

# print(read_file_txt("authors.txt"))

# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)


def get_dey_fromstring(string):
    dayin = r"\d{1,2}[a-z]{2}"  # c отстатком букв
    if len(re.findall(dayin, string)[0][:-2]) == 1:
        return "0" + re.findall(dayin, string)[0][:-2]
    else:
        return re.findall(dayin, string)[0][:-2]


def get_year_fromstring(string):
    yearin = r"\d{4}"
    return re.findall(yearin, string)[0]


def change_month_name_to_number(string):
    month_in_year = {"January": "01",
                     "February": "02",
                     "March": "03",
                     "April": "04",
                     "May": "05",
                     "June": "06",
                     "July": "07",
                     "August": "08",
                     "September": "09",
                     "October": "10",
                     "November": "11",
                     "December": "12"}
    for month in month_in_year:
        if month in string:
            return month_in_year[month]


def create_dict_from_string(data):
    dict_list = []
    author_name = r"-.+\w+\b's"
    for string in data:
        dict_list.append({"name": (re.findall(author_name, string))[0][2:-2], "date": get_dey_fromstring(string) + "/" + change_month_name_to_number(string) + "/" + get_year_fromstring(string)})

    return dict_list

# print(create_dict_from_string(read_file_txt("authors.txt")))

# Написать функцию, которая сохраняет результат пункта 2.2 в json файл


def write_json_file(data, filename="test2.json"):
    with open(filename, "w") as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)


write_json_file(create_dict_from_string(read_file_txt("authors.txt")))
