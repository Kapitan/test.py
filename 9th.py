import csv
import json
def read_txt(fille):
    with open(fille, "r") as ffile:
        data = []
        for line in ffile.readlines():
            data.append(line.strip())
    return data


def read_json(fille):
    with open(fille, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def read_csv(fille):
    with open("test.csv", "r") as csv_file:
        data = []
        reader = csv.DictReader(csv_file, delimiter=";")
        for row in reader:
            data.append(row)
    return data


def read_file(file_name):
    ext = file_name.split(".")[-1]
    if ext == "txt":
        res = read_txt(file_name)
    elif ext == "json":
        res = read_json(file_name)
    elif ext == "csv":
        res = read_csv(file_name)
    else:
        print("incorret filetype")
    return res


result_txt = read_file("domains.txt")
result_json = read_file("ttt.json")
result_csv = read_file("test_new.csv")

print(result_txt)



# with open("test.csv", "r") as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=";")
#     data = []
#     for r in reader:
#         data.append(r)
#
# print(data)

# with open("test.csv", "r") as csv_file:
#     data = []
#     reader = csv.reader(csv_file, delimiter=";")
#     for row in reader:
#         data.append(row)
#
# print(data)

# data.append({'name':"5789698696", 'e-mail':"erfgbnfy.@test2", "text" : "7777"})

# with open("test_new.csv", "w") as secfile:
#     fieldnames = data[0].keys()
#     writer = csv.DictWriter(secfile,  fieldnames=fieldnames, delimiter=",")
#     writer.writeheader()
#     writer.writerows(data)


# with open("ttt.json", "r", encoding="utf-8") as json_file:
#     data = json.load(json_file)
#
# # print(data)
#
# data["test_key"] = "test_value"
# print(data)
#
# with open("ttt2.json", "w") as json_file2:
#     json.dump(data, json_file2, indent=2)
