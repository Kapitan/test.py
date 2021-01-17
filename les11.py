# import os
# import string
#
# def tanos_click(dirname):
#     files = sorted([file for file in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, file))])
#     for file in list(set(files))[:len(files) // 2]:
#         os.remove(os.path.join(dirname, file))
#
# def create_txt_file(dirname):
#     for simbol in string.ascii_lowercase:
#         file_name = os.path.join(dirname, f"{simbol}.txt")
#         write_file(file_name, string.ascii_lowercase.replace(simbol, simbol.upper()))
#
#
# def write_file(filename, data):
#     with open(filename, "w") as txt_file:
#         txt_file.write(data)
#
# def create_dir(dir_name):
#     try:
#         os.mkdir(dir_name)
#     except FileExistsError:
#         pass
#
#
# dir_mane1 = "alphabet1"
# #create_dir(dir_mane1)
# create_txt_file(dir_mane1)
# #tanos_click(dir_mane1)

# =======================

# sort function

# test_list = ["asd", "sdgg", "zxc", "q", "we"]
# new_list = sorted(test_list, key=len)
# print(new_list, test_list)
#
# numb_list = [1,2,3,4,-3,-30, 44]
# new_numb_list = sorted(numb_list, key=abs)
# print(new_numb_list)
import re
def key_sorted_by_age(obj_dict):
    ages = re.findall(r"[0-9]+", obj_dict["age"])
    return int(ages[-1])


def key_sorted_by_name(obj_dict):
    return obj_dict["name"]


def key_sorted_by_name_length(obj_dict):
    return len(obj_dict["name"])


dict_list = [
    {"name": "Johnddd", "age": "1945 - 1977"},
    {"name": "Vinnie", "age": "1988 - 1999"},
    {"name": "Joh", "age": "1900 - 1966"}
]

new_dict_list = sorted(dict_list, key=key_sorted_by_age)
print(new_dict_list)
