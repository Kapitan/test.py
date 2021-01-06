import string
import random

def random_word(length):
    w = []
    w.append(random.choice(string.ascii_letters))
    w += [random.choice(string.ascii_lowercase) for _ in range(length-1)]
    return "".join(w)

def random_int(length):
    e = [random.choice(string.digits) for _ in range(length)]
    return "".join(e)

print(random_int(random.randint(1,10)))
print(random_word(random.randint(0,10)))

data = []
for i in range(50):
    t = random.randint(0, 25)
    if t <= 10:
        data.append(random_word(random.randint(0, 10)) + " ")
    elif 10 < t <= 20:
        data.append(random_int(random.randint(1,5)) + " ")
    else:
        data.append("\n")

print("".join(data))
