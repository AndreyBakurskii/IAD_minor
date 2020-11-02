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


STRING = "hello"
LEN_RETURN_STR = len(STRING)
REPEAT = False

print(*possible_strings(STRING, LEN_RETURN_STR, REPEAT))
