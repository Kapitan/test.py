import random


def create_text_line(min_len, max_len):
    txt_list = [chr(random.randint(ord('a'), ord('z'))) for _ in range(random.randint(min_len, max_len))]
    return "".join(txt_list)


def create_number_line(min_len, max_len):
    txt_list = [chr(random.randint(ord('0'), ord('9'))) for _ in range(random.randint(min_len, max_len))]
    return "".join(txt_list)


def split_text_line(txt_line):
    space_count = len(txt_line) // 10
    space_index_list = []
    while len(space_index_list) < space_count:
        index = random.randint(1, len(txt_line) - 2)
        if (index not in space_index_list and
                index - 1 not in space_index_list and
                index + 1 not in space_index_list):
            space_index_list.append(index)
    for index in space_index_list:
        txt_line = txt_line[:index] + " " + txt_line[index + 1:]
    return txt_line


def replace_text_to_number(word):
    if len(word) > 5:
        return word
    else:
        return create_number_line(len(word), len(word))


def replace_first_letter(word):
    return word.replace(word[0], word[0].upper(), 1)


def replace_last_letter(word):
    signs = ',.;:!?'
    if len(word) < 4:
        return word
    else:
        return word[:-1] + random.choice(signs)


def create_randome_txt_data(min_len=100, max_len=1000):
    txt_line = create_text_line(min_len, max_len)
    txt_line = split_text_line(txt_line)
    new_words = []
    for word in txt_line.split():
        case = random.randint(1, 100)
        if not case % 10:
            new_word = replace_text_to_number(word)
        elif not case % 2:
            new_word = replace_first_letter(word)
        elif not case % 5:
            new_word = replace_last_letter(word)
        else:
            new_word = word
        new_words.append(new_word)
    # word = txt_line.split()[0]
    # print(word, replace_last_letter(word))
    return " ".join(new_words)

print("__name__ >>>", __name__)

number =150

if __name__ == "__main__":
    txt_data = create_randome_txt_data()
    print("!!!!!!!!!!!!!!!", txt_data)
