# mystr = "testrt ,.dkuhs#%^dfvli hawdtfba efbdtfb diff"
# print(len(mystr))
# if "t" in mystr:
#     print("huy")
# print(f" я строка {mystr},
# x = mystr[1] = "qqq"


# 1) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно половине значения value, в противном случае - противоположне value число
value = 200
new_value = value / 2 if value < 100 else 0 - value
print(new_value)
# 2) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно 1, в противном случае - 0
new_value = 1 if value < 100 else 0
print(new_value)
# 3) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу:
# если value меньше 100, то new_value равно True, в противном случае - False

new_value = True if value < 100 else False
print(new_value)
# 4) У вас есть переменная my_str, тип - str.
# Заменить в my_str все маленькие буквы на большие.
my_str = "Test MY NeW string and ChanGE LatterS"
my_str = my_str.upper()
print(my_str)
# 5) У вас есть переменная my_str, тип - str.
# Заменить в my_str все большие буквы на маленькие.
my_str = "Test SecOnd MY NeW string and ChanGE LatterS"
my_str = my_str.lower()
print(my_str)
# 6) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же.
# Пример: было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.
my_str = "Test"
my_str = my_str + my_str if len(my_str) < 5 else my_str
print(my_str)
# 7) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же.
# Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.
my_str = "Test"
my_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(my_str)
# 8) У вас есть переменная my_str, тип - str.
# Вывести на экран все символы из этой строки, которые являются буквой или цифрой.
my_str = "Test 3d MY$ NeW str1ng? w1th numb3r5 #and LatterS"
for i in my_str:
    if i.isalnum():
        print(i)
# 9) У вас есть переменная my_str, тип - str.
# Вывести на экран все символы из этой строки, которые не являются буквой или цифрой.
for x in my_str:
    if not x.isalnum():
        print(x)
# 10) У вас есть переменная my_str, тип - str.
# Вывести на экран все символы из этой строки, которые не являются буквой или цифрой и не пробел.
for z in my_str:
    if not z.isalnum() and z != " ":
        print(z)
