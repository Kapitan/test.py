# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).
import requests
import csv

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
        if (not r in x) and (r["quoteAuthor"] != ''):
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

#write_csv_file(get_uniq_q_in_list(30))

# 2. Дан файл authors.txt
# 2.1) написать функцию, которая считывает данные из этого файла,
# возвращая СПИСОК тех строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.
import re

def read_file_txt(filename):
    list_of = []
    reg = r"\d{1,2}[a-z]{2}\s[A-Z][a-z]{2,8}\s\d{4}"
    reg2 = r"-.+\w+\b's"
    with open(filename, "r") as filetxt:
        for strings1 in filetxt.readlines():
            if (("birthday" in strings1.lower()) or ("death" in strings1.lower())) and re.findall(reg, strings1) and re.findall(reg2, strings1):
                list_of.append(strings1)
    return list_of

print(len(read_file_txt("authors.txt")))

# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
