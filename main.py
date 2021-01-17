import string
import random
import json
import csv


def random_word(length):
    w = []
    w.append(random.choice(string.ascii_letters))
    w += [random.choice(string.ascii_lowercase) for _ in range(length-1)]
    return "".join(w)


def random_int(length):
    e = [random.choice(string.digits) for _ in range(length)]
    return "".join(e)


def replace_last_letter(word):
    signs = ',.;:!?'
    if len(word) < 4:
        return word
    else:
        return word[:-1] + random.choice(signs)


def text_creaate(count_of_words):
    data = []
    for i in range(count_of_words):
        data.append(random.choice([random_word(random.randint(0, 10)) + " ", random_int(random.randint(1,5)) + " ", "\n" + random_word(random.randint(0, 10)) + " ", replace_last_letter(random_word(random.randint(0, 10))) + " "]))
    data2 = "".join(data)
    return data2

#random_word(5).lower()


def random_value():
    counts = [random.randint(-100, 100), random.random(), random.choice([True, False])]
    return random.choice(counts)


def creaate_dict(length):
    return {random_word(5).lower(): random_value() for _ in range(length)}


def create_list_for_csv(rows, colm):
    main_list = []
    for _ in range(rows):
        colm_list = []
        for _i in range(colm):
            colm_list.append(random.choice([0, 1]))
        main_list.append(colm_list)
    return main_list


# print(create_list_for_csv(6,5))
# print(creaate_dict(random.randint(5, 20)))

def write_file_txt(path):
    with open(path, "w") as txtfile:
        txtfile.write(text_creaate(100))


def write_file_json(path):
    with open(path, "w") as jsonfile:
        json.dump(creaate_dict(random.randint(5, 20)), jsonfile)


def write_file_csv(path):
    with open(path, "w") as filecsv:
        writer = csv.writer(filecsv, delimiter=',')
        for t in create_list_for_csv(random.randint(3,10), random.randint(3,10)):
            writer.writerow(t)
            print(t)



def write_file(file_name):
    ext = file_name.split(".")[-1]
    if ext == "txt":
        write_file_txt(file_name)
    elif ext == "json":
        write_file_json(file_name)
    elif ext == "csv":
        write_file_csv(file_name)
    else:
        print("Unsupported file format")


write_file("1.aefg")
