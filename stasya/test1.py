import random
import string
import json
import csv
# Функция 1. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# Знаки препинания всегда идут в конце слова.
#
# str1 = [chr(random.randint(ord('a'), ord('z'))) for _ in range(random.randint(100, 1000))]
# str2 = ''.join(random.choices(string.ascii_uppercase + " ,.;:!?" + string.ascii_lowercase + string.digits + '\n', k=(random.randint(ord('a'), ord('z'))) ))
# print(str2)

def random_word(length):
    word = []
    word.append(random.choice(string.ascii_letters))
    word += [random.choice(string.ascii_lowercase) for symbol in range(length-1)]
    return "".join(word)

def random_int(length):
    digits = [random.choice(string.digits) for symbol in range(length)]
    return "".join(digits)

def replace_last_letter(word):
    signs = ',.;:!?'
    if len(word) < 4:
        return word
    else:
        return word[:-1] + random.choice(signs)

def text_create(countOfwords):
    data = []
    for i in range(countOfwords):
        data.append(random.choice([random_word(random.randint(0, 10)) + " ", random_int(random.randint(1,10)) + " ", "\n" + random_word(random.randint(0, 10)) + " ", replace_last_letter(random_word(random.randint(0, 10))) + " "]))
    data2 = "".join(data)
    return data2

print(text_create(100))


# Функция 2. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.

def create_value():
    return random.choice([random.randint(-100, 100), random.random(), random.choice([True, False])])

def create_dict(length):
    return {random_word(5).lower(): create_value() for i in range(length)}

# Функция 3. Создает данные для записи в файл csv.
# Создает и возвращает список длинны n внутренних списков длинны m (таблица с n строк и m столбцов).
# Числа n и m выбираются случайно в диапазоне от 3 до 10.
# В таблицу записывать значения только 0 или 1.
# Заголовка у таблицы нет.

def create_list(m, n):
    list = []
    for i in range(m):
        nlist = []
        for x in range(n):
            nlist.append(random.choice([0, 1]))
        list.append(nlist)
    return list

# А теперь основное задание:
# Написать функцию generate_and_write_file которая принимает один параметр - полный путь к файлу.
# В зависимости от расширения файла (txt, csv, json) сгенерировать данные для записи и записать в данный файл.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"

def write_txt(path):
    with open(path, 'w') as txtfile:
        txtfile.write(text_create(100))

write_txt('hom9.txt')

def write_json(path):
    with open(path, 'w') as jsonfile:
        json.dump(create_dict(random.randint(5, 20)), jsonfile)


write_json('hom9.json')

def write_csv(path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for i in create_list(random.randint(3, 10), random.randint(3, 10)):
            writer.writerow(i)
            print(i)

write_csv('hom9.csv')

# def generate_and_write_file:
#     ext = filename.split(".")[-1]
#     if ext == 'txt':
#         result = read_txt(filename)
#     elif ext == "json":
#         result = read_json(filename)
#     elif ext == "csv":
#         result = read_csv(filename)
#     else:
#         print = ('Unsupported file format')
#         result = ''
#     return result
