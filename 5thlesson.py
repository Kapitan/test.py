# 3a. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
#
# 3b. Даны списки my_list_1 и my_list_2. Создать список my_result в который
# вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# my_list_1 = [1,2,3,4,5], my_list_2 = [10, 15, 20, 25] -> my_result [2, 4, 15, 25]
#
# my_list_1 = ["q", "w", "e", "r"]
# my_list_2 = [1, 2, 3, 4]
# my_result = []
# # my_result.
# mya = 123897598745
# ert = list(str(mya))
# ert.sort()
# res = (ert.sort())
#
# # value_list = list(str(value))
# # value_list.sort()  # сортировка списка
# # res = int("".join(value_list))
# print(res)
ascii_table = {number: chr(number) for number in range(ord('a'), ord('z') + 1)}
print(ascii_table.items())
for key in ascii_table:
    print(key)
