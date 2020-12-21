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
my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [10, 15, 20, 25, 33]
my_result = []
for i in my_list_1:
    if not i % 2:
        my_result.append(i)

for i in my_list_2:
    if i % 2:
        my_result.append(i)

print(my_result)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
my_list4 = [1,2,3,4]
new_list = my_list4.copy()
new_list.append(new_list[0])
new_list.remove(new_list[0])
print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
mylist5 = [8, 1, 2, 3, 4, 5, 6]
mylist5.append(mylist5.pop(0))
print(mylist5)


# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133.

my_str6 = "43 больше чем 34 но меньше чем 56"

word_list = my_str6.split()
num_list = []
number_last = 0
for word in word_list:
    if word.isnumeric():
        num_list.append(int(word))

for value in num_list:
    number_last += value
print(number_last)




my_str7 = 'gfdsqgzer'
if len(my_str7) % 2:
    my_str7 += "_"
print([my_str7[index:index + 2] for index in range(0, len(my_str7), 2)])

# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить часть строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"
my_str8 = "My_long str"
l_limit = "o"
r_limit = "t"

mystr_test = list(my_str8)
mysubstr = "".join(mystr_test[mystr_test.index(l_limit) + 1:mystr_test.index(r_limit)])

print(mysubstr)


# 9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
my_str9 = "My long string"
l_limit9 = "o"
r_limit9 = "g"

_ = list(my_str9)
_2 = _.copy()
_2.reverse()
indexofr_imit = len(_2) - _2.index(r_limit9) - 1
print(indexofr_imit)

splitstr9 = "".join(_[_.index(l_limit) + 1:indexofr_imit])
print(splitstr9)



# 10. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

list10 = [2, 4, 1, 5, 3, 9, 0, 7, 2, 0]
new_list = []
for i,value in enumerate(list10):
    if i == 0 or i == len(list10) - 1:
        continue
    elif value > list10[i - 1] + list10[i + 1]:
        new_list.append(value)

print(len(new_list))
