import csv
import json
with open("test.csv", "r") as csv_file:
    data = []
    reader = csv.reader(csv_file, delimiter=";")
    for row in reader:
        data.append(row)

print(data)

data.append([56, "ererererer.@test2", 7777])

with open("test_new.csv", "w") as secfile:
    writer = csv.writer(secfile, delimiter=",")
    writer.writerows(data)


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
