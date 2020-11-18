def print_error(text):
    print("\033[31m" + "ERROR :: " + str(text))
    print("\033[0m", end="")


def print_error_phone(text):
    print_error("PHONE :: " + str(text))


def print_error_firstname(text):
    print_error("FIRSTNAME :: " + str(text))


def print_error_lastname(text):
    print_error("LASTNAME :: " + str(text))


def print_error_birthday(text):
    print_error("BIRTHDAY :: " + str(text))


def print_warning(text):
    print("\033[93m" + "WARNING :: " + str(text))
    print("\033[0m", end="")


def print_warning_record(text):
    print_warning("RECORD :: " + str(text))


def do_first_letter_upper(string: str):
    return string[0].upper() + string[1:]
