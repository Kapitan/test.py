# 1. Считать данные из файла domains.txt
# Названия интернет доменов поместить в список (названия сохранить без точки).
#
# 2. Считать данные из файла names.txt и поместить в список только фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.
#
# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2 и переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, так как буквы не смогут повторяться)
#
# Пример вызова функции:
# e_mail = create_email(domains, names)
# print(e_mail)
#
# >>>miller.249@sgdyyur.com
import random
import string

with open("./domains.txt", "r") as domanes:
    domain_list = []
    for strings in domanes.readlines():
        domain_list.append(strings[1:-1])

print(domain_list)

with open("./names.txt", "r") as names:
    name_list = []
    for strings1 in names.readlines():
        name_list.append(strings1.split()[1])
        #print(strings1.split()[1])

print(name_list)

def create_e_mail(d_list, n_list):
    part2 = random.randint(100, 999)
    part1 = random.choice(n_list)
    part4 = random.choice(d_list)
    part3 = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(5, 7)))
    return part1.lower() + "." + str(part2) + "@" + part3 + "." + part4

test_one = create_e_mail(domain_list, name_list)

print(string.ascii_uppercase)
