from random import random


def point_a(ver: float, len_vyb=1) -> int or list:

    return [int(random() < ver) for i in range(len_vyb)] if len_vyb > 1 else int(random() < ver)


def point_b(ver: float, kol_exp: int, len_vyb=1) -> int or list:
    return [sum(point_a(ver=ver, len_vyb=kol_exp)) for i in range(len_vyb)] if len_vyb > 1 else\
            sum(point_a(ver=ver, len_vyb=kol_exp))


print(point_a(0.6, len_vyb=1))
print(point_a(0.6, len_vyb=4))

print(point_b(0.7, 3, len_vyb=1))
print(point_b(0.7, 3, len_vyb=4))
