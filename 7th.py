# # # ascii = {number: chr(number) for number in range(ord('a'), ord('z') + 1)}
# # # print(ascii)
# # #
# # # key = 130
# # # # if key in ascii:
# # # #     print(ascii[key])
# # #
# # # print(ascii.get(key))
# # #
# # # # for i in ascii:
# # # #     print(i)
# # # #
# # # print(ascii.keys(), type(ascii.keys()))
# # # print(ascii.values(), type(ascii.values()))
# # # print(ascii.items(), type(ascii.items()))
# # my_list = [1, 2, 4]
# # val1, val2, val3 = my_list
#
# # 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# # Задание можно выполнить и через обычный цикл и через генератор списков.
# import random
#
# new_list = []
# for i in range(20):
#     new_list.append(random.randint(1, 100))
#
# # print(new_list)
#
# a = [random.randint(1, 100) for i in range(20)]
# # print(a)
# # 2) Создать словарь triangle в который записать точки A B C (ключи),
# # и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -100 до 100 по каждой оси.
#
# def point():
#     return tuple([random.randint(-100, 100) for i in range(3)])
#
# triangle = {"A": point(), "B": point(), "C": point()}
#
#
# # for key in triangle:
# #     triangle[key] = tuple([random.randint(-100, 100) for i in range(3)])
#
#
#
# print(triangle)
#
#
# # 3) Создать функцию print_stars, которая принимает в виде параметра строку и печатает ее
# # с тремя символами * вначале и в конце строки.
# # Пример:
# # my_str = "I'm the string"
# # print_stars(my_str)
# # Печатает ***I'm the string***
#
# def stars(mystr):
#     print(f"***{mystr}***")
#
#
# stars("one two")
#
#
# # Задания 4 и 5 выполнять с помощью циклов
# # 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# # а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена с этим возрастом.
# # б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена этой длинны.
# # в) Посчитать среднее количество лет всех людей из списка.
#
# dict_list = [{"name": "John", "age": 55}, {"name": "Jack", "age": 45}, {"name": "Jac", "age": 55}, {"name": "Jacky", "age": 45}]
# test_list = []
# yongest = ""
# for x in dict_list:
#     test_list.append(x["age"])
# test_list.sort()
# for x in dict_list:
#     if x["age"] == test_list[0]:
#         print("shortest " + x["name"])
#
# for x in dict_list:
#     if x["age"] == test_list[-1]:
#         print("longest " + x["name"])
#
# average_age = 0
# for i in test_list:
#     average_age += i
# average_age /= len(test_list)
# print(average_age)
#


# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},


dict1 = {"one": "1",
         "two": "2",
         "tree": "3"}
dict2 = {"tree": "33",
         "four": "4",
         "two": "22",
         "five": "5"}

list_keys = []
for x in dict1:
    if x in dict2:
        list_keys.append(x)

print(list_keys)

list_keys2 = []
new_dict = {}
new_dict2 = {}
for c in dict1:
    if c not in dict2:
        list_keys2.append(c)
        new_dict.update({c : dict1[c]})




print(list_keys2)
print(new_dict)
new_dict2.update(dict1)
new_dict2.update(dict2)

for b in dict1:
    if b in dict2:
        new_dict2[b] = [dict1[b], dict2[b]]
print(new_dict2)
