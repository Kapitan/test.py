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

def replace_last_letter(word):
    signs = ',.;:!?'
    if len(word) < 4:
        return word
    else:
        return word[:-1] + random.choice(signs)

def text_creaate(countOfSymb):
    data = []
    for i in range(countOfSymb):
        data.append(random.choice([random_word(random.randint(0, 10)) + " ", random_int(random.randint(1,5)) + " ", "\n" + random_word(random.randint(0, 10)) + " ", replace_last_letter(random_word(random.randint(0, 10))) + " "]))
    data2 = "".join(data)
    return data2



print(text_creaate(100))

