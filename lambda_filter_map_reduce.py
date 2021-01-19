# import re
#
# test_str = "my e-mail is akapitan@eva.ua and 123192.168.3.5 and 12345.123 and 10.100.20.20"
#
# ip_add = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
#
# emailre = r"\w+@[a-z]+\.[a-z]+"
# reg_exp = r"."
#
# print(re.findall(ip_add, test_str))

#сортировка

result_1 = (lambda x: x + 3)(4)

#print(result_1)

def testf(x):
    return x + 3

#print(testf(4))

add_function = lambda x, y:x + y
result_2 = add_function(4,5)

result_3 = (lambda x,y,z: x + y + z)(1,2,3)
result_5 = (lambda *args: sum(args))(1,3,4,5,6,7,8)

#filter

data = [2, 63, 7, 8, 196, 6, 99]
print([n for n in data if n % 2])

data2 =list(map(str, data))
print(data2)

def fil_fun(n):
    return n % 2

print(list(filter(fil_fun, data)))

print(list(filter(lambda x: x % 2, data)))



##reduce
from functools import reduce
datered = [1,4,5,6,8,33,44,6]



result = reduce(lambda maindata, x: maindata + x, datered, 0)
print(result)

myresult = 0
for i in datered:
    myresult += i

print(myresult)
