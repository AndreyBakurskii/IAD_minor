from math import factorial
from random import randint


def main_func(string: str, len_return_str: int, repeat: bool) -> str or None:

    len_string = len(string)

    if not repeat and len_string < len_return_str:
        return

    # определение количества всевозможных строк
    n = 0

    if repeat:
        n = len_string ** len_return_str
    else:
        n = factorial(len_string) / factorial(len_string - len_return_str)

    # список всевозможных строк
    data_possible_strings = possible_strings(string, len_return_str, repeat)

    # выбор случайной строки
    number_string = randint(1, n)

    return data_possible_strings[number_string]


def possible_strings(string: str, len_return_str: int, repeat: bool) -> list:

    if len_return_str == 1:
        return [char for char in string]

    result = []

    if repeat:
        for ind, elem in enumerate(string):
            result.extend([elem + s for s in possible_strings(string, len_return_str - 1, repeat)])

    else:
        for ind, elem in enumerate(string):
            result.extend([elem + s for s in possible_strings(string[:ind] + string[ind + 1:], len_return_str - 1, repeat)])

    return [elem for elem in set(result)]


print(main_func("abc", 5, True))
