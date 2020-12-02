# new_skug tr = input("add new integer: ")
# newint = int(new_str)
# try:
#     newint = int(new_str)
#     value = 88 / newint
#     print(value)
# except ValueError:
#     print("введите только число")kgbkjbkjbjkbiuguig
# except ZeroDivisionError:
#     print("can not delet eto na zero")

# s   tring = "lahsdlvb"
# print(tuple(string))

# my_tuple k = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# tupl_str = ("qwe", "rty", "bgt6")
#
# from typing import List, Union, Tuple

server_codes = ("200", "404", "403", "301", "302", "502")

# # prin t(server_codes[2:len(server_codes)])
# print(my_tuple[-2:-5:-1])
#
# x = (2, 5, 9, 7, "f", True)
#
# a, z, *p = x
#
# print(p)


# my_li st = ["9", "7", 'f', "True", "tr"]
# my_list.insert(3, "хуй")
# my_list.append(server_codes)
# print(my_list)
# my_list.remove(server_codes)
# last = my_list.pop(2)
# print(last)

# my_st r = "sfjh lkh lkhkhasef  wetkh kgkhmhv "
# # print(list(my_str))
# print(my_str.split(" "))
#
# x = ' '.join(my_list)
# print(x)


# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.
my_list = [23, 400, 150, 56, 211]
for i in my_list:
    if i > 100:
        print(i)

# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.
my_results = []
for i in my_list:
    if i > 100:
        my_results.append(i)
print(my_results)

# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

my_list.append(0) if len(my_list) < 2 else my_list.append(my_list[-1] + my_list[-2])
print(my_list)

# 4) Пользователь вводит value - число с запятой (например 3.14) с клавиатуры.
# Вы приводите это value к типу float и выводите результат выражения value ** -1.
# Написать программу, которая вычисляет данное выражение и
# корректно обрабатывает возможные исключения.

# val = input("enter 2.4 ")
# try:
#     result = float(val) ** -1
#     print(result)
# except ValueError:
#     print("enter valid float with dot '.'")
# except ZeroDivisionError:
#     print("0.0 cannot be raised to a negative power")


# 5) У вас есть список значений my_list и список индексов my_indexes
# (начинается с нуля и количество элементов совпадает с количеством в my_list.
# Распечатать значения из my_list через обращение по индексу. См. пример выше.

# 6) У вас есть два списка my_list_1 и my_list_2 равной длинны и
# список индексов my_indexes (начинается с нуля и количество элементов
# совпадает с количеством в my_list_1.
# Распечатать пары значений из my_list_1 и my_list_2 через обращение по индексу.

my_list_1 = ["q", "w", "e", "r", "t", "y"]
my_list_2 = ["a", "s", "d", "f", "g", "h"]
ind = [0, 1, 2, 3, 4, 5]

for i in ind:
    print((my_list_1[i], my_list_2[i]))

# 7) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов .
# Генерирование через range или другие "фишки" я засчитывать не буду ))

my_string = '0123456789'
new_list = []
for i in my_string:
    for x in my_string:
        new_list.append(int(i + x))

print(new_list)
