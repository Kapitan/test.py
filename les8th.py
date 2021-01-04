import random
import string

with open("./rec.py", "r") as py_file:
    data = []
    for strings in py_file.readlines():
        data.append(strings.strip())

for line in data:
    print(line)

data.append("yyyyyyyyy")

with open("./rec.py", "w") as wright_file:
    wright_file.write("\n".join(data))




# def crate_random_point(min_lim, max_lim):
#     point = (random.randint(min_lim, max_lim),
#              random.randint(min_lim, max_lim),
#              random.randint(min_lim, max_lim))
#     return point
#
#
# def create_line_segment(ww, ww2):
#     line_segment = {"A": crate_random_point(ww, ww2),
#                     "B": crate_random_point(ww, ww2)}
#     return line_segment
#
# A = crate_random_point(-100, 100)
# B = crate_random_point(-100, 100)
# print(A)
# print(B)
#
# AB = create_line_segment(-2, 10000)
# print(AB)
# # print(type(string.ascii_lowercase))
# def create_rand_str(str_len, debugmod=False):
#     rand_str = list(string.ascii_lowercase)
#     random.shuffle(rand_str)
#     # "".join(rand_str[:str_len])
#     if debugmod:
#         print("".join(rand_str[:str_len]))
#     return "".join(rand_str[:str_len])
#
#
# create_rand_str(8)
# # print(create_rand_str(8))
