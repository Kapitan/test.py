import random

def crate_random_point(min_lim, max_lim):
    point = (random.randint(min_lim, max_lim),
             random.randint(min_lim, max_lim),
             random.randint(min_lim, max_lim))
    return point


def create_line_segment(ww, ww2):
    line_segment = {"A": crate_random_point(ww, ww2),
                    "B": crate_random_point(ww, ww2)}
    return line_segment

A = crate_random_point(-100, 100)
B = crate_random_point(-100, 100)
print(A)
print(B)

AB = create_line_segment(-2, 10000)
print(AB)
