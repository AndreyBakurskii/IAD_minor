def print_error(text):
    """
    Выводит сообщение об ошибке красным цветом.

    :param text: сообщение об ошибке (str)
    :return:
    """
    print("\033[31m" + "ERROR :: " + str(text), end="\n")
    print("\033[0m", end="")


def print_warning(text):
    """
    Выводит предупреждение желтым цветом.
    :param text: текст предупреждения (str)
    :return:
    """
    print("\033[93m" + "WARNING :: " + str(text))
    print("\033[0m", end="")


def do_first_letter_upper(string: str):
    """
    Форматирует полученную строку - возведение первой буквы в верхний регистр.
    :param string: строка, подлежащая форматированию (str)
    :return: отформатированная строка (str)
    """
    return string[0].upper() + string[1:]
