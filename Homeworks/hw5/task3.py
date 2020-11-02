def possible_strings(string: str) -> list:
    """
    Создает всевозможные строки из элементов строки string путем перестановки
    :param string: искомая строка
    :return: список всевозможных строк из элементов string
    """

    if len(string) == 2:
        return [string, string[::-1]]

    if len(string) == 1:
        return [string]

    result = []

    for ind, elem in enumerate(string):
        result.extend([elem + s for s in possible_strings(string[:ind:] + string[ind + 1:])])

    # убираем повторяющиеся строки и возвращаем результат функции
    return [s for s in set(result)]


STRING = "hello"

print(*possible_strings(STRING))
