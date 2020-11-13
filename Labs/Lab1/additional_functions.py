def print_error(text):
    print("\033[31m" + "ERROR :: " + str(text))


def usual_print(text):
    print("\033[0m" + str(text))


def print_error_phone(text):
    print_error("PHONE :: " + str(text))


def print_error_firstname(text):
    print_error("FIRSTNAME :: " + str(text))


def print_error_lastname(text):
    print_error("LASTNAME :: " + str(text))


def print_error_birthday(text):
    print_error("BIRTHDAY :: " + str(text))
