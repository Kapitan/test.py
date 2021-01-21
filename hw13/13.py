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


# Основа ДЗ - ДЗ №8 https://github.com/30nt/IntroPython_18_11/blob/main/Homeworks/lesson8.txt
#
# Суть задания - сздать класс EmailGenerator
#
# 1. При инициализации класса передавать два параметра - путь к файлу domains.txt и путь к файлу names.txt
# Пример:
# email_generator = EmailGenerator("domains.txt", "names.txt")
#
# 2. Атрибуты экземпляра класса: domains и names.
# Получаются с помощью методов get_domains() и get_names(). (описание и реализацию нужно взять из ДЗ №8)
# Пример:
# self.domains = self.get_domains()
# self.names = self.get_names()
#
# 3. При выводе на печать экземпляра класса вывести количество элементов в атрибутах domains и names
# Пример:
# print(email_generator)
# >>>len domains = 8, len names = 34
#
# 4. Написать метод экземпляра класса generate_email() (описание и реализацию нужно взять из ДЗ №8)
# Пример:
# email = email_generator.generate_email()
# print(email)
# >>>miller.249@sgdyyur.com

import random
import string


class EmailGenerator:
    def __init__(self, path_file_d, path_file_n):
        self.path_file_d = path_file_d
        self.path_file_n = path_file_n
        self.domains = self.get_domains()
        self.names = self.get_names()

# 3. При выводе на печать экземпляра класса вывести количество элементов в атрибутах domains и names
# Пример:
# print(email_generator)
# >>>len domains = 8, len names = 34

    def __str__(self):
        return f"len domains = {len(self.get_domains())}, len names = {len(self.get_names())}"

    def get_domains(self):
        domain_list = []
        with open(self.path_file_d, "r") as domains:
            for strings in domains.readlines():
                domain_list.append(strings[1:-1])
        return domain_list

    def get_names(self):
        name_list = []
        with open(self.path_file_n, "r") as names:
            for strings1 in names.readlines():
                name_list.append(strings1.split()[1])
        return name_list

# 1) максимальное значение числа после имени от 100 до ...
# 2) максимальное значение домена 2 уровня от 5 до ....

    def generate_email(self, maxint=999, maxdom=7):
        part2 = random.randint(100, maxint)
        part1 = random.choice(self.get_names())
        part4 = random.choice(self.get_domains())
        part3 = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(5, maxdom)))
        return part1.lower() + "." + str(part2) + "@" + part3 + "." + part4


test = EmailGenerator("domains.txt", "names.txt")

#print(test.names)
