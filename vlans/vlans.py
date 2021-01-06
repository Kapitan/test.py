import csv
scvnow = []
with open("VLANs.csv", "r") as csv_vlan:
    csvreader = csv.reader(csv_vlan)
    for i in csvreader:
        scvnow.append(i)
#print(scvnow)
data = []
data2 = []
with open("aruba.conf", "r") as config:
    confreader = config.readlines()
    for k, v in enumerate(confreader):
        if v.split()[0] == "vlan":
            c = v.split()
            c.append(confreader[k+1].split()[1][1:-1])
            data.append(c)

#print(data)
for q in data:
    c = [q[2], '', q[1], q[1], "4" ]
    data2.append(c)

scvnow += data2
print(scvnow)

with open("newv.csv", "w") as newv:
    writer = csv.writer(newv, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)
    for t in scvnow:

        writer.writerow(t)

