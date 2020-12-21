import random


# import random as rnd
# from random import randint, choice, shuffle
def x():
    my_var = random.randint(-10, 10)
    return my_var


def crate_random_point():
    point = (x(),
             x(),
             x())
    return point


def create_line_segment():
    line_segment = {"A": crate_random_point(),
                    "B": crate_random_point()}
    return line_segment


def print_line_segment(line_segment):
    print(f"Отрезок AB: {line_segment['A']}, {line_segment['B']}")


number = random.randint(1, 10)
# number = rnd.randint(1, 10)
# number2 = randint(1, 10)
print(number)

AB = {"A": (random.randint(-10, 10),
            random.randint(-10, 10),
            random.randint(-10, 10)),
      "B": (random.randint(-10, 10),
            random.randint(-10, 10),
            random.randint(-10, 10)),
      }
# print(AB)
#
# print(random.choice(AB)) ## подумать как сделать choice из словаря

my_str = list("qwerty")
random.shuffle(my_str)
print(my_str)
print(random.choice(my_str))
# Принцип DRY (Dont repeat yourself) Не повторяйся!


AB = create_line_segment()
print_line_segment(AB)
