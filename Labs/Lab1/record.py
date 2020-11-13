import re as re
from prettytable import PrettyTable
import Labs.Lab1.additional_functions as add_func
import time


class Record:

    def __init__(self, firstname: str, lastname: str, phone: str, birthday=""):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.birthday = birthday

    def __str__(self):
        return f"{self.firstname} | {self.lastname} | {self.phone} | {self.birthday}"

    def __repr__(self):
        return f"Firstname: {self.firstname}\n" \
               f"Lastname: {self.lastname}\n" \
               f"Phone: {self.phone}\n" \
               f"Birthday: {self.birthday if self.birthday else 'not defined'}\n"

    def conv2dict(self) -> dict:
        return {
                "firstname":    self.firstname,
                "lastname":     self.lastname,
                "phone":        self.phone,
                "birthday":     self.birthday
                }

    def get_values(self):
        return [self.firstname, self.lastname, self.phone, self.birthday]


class SetRecords:

    def __init__(self, list_records: list):
        self.list_records = list_records

    def __str__(self):
        table = PrettyTable(["№", "Firstname", "Lastname", "Phone", "Birthday"])
        table.align["N"] = 'l'

        for ind, record in enumerate(self.list_records):

            row = [str(ind)]
            row.extend(record.get_values())

            table.add_row(row)

        return table.get_string()


def parse_record(data: dict) -> Record:
    firstname, lastname, phone, birthday = data.values()

    return Record(firstname, lastname, phone, birthday=birthday)


def check_firstname_or_lastname(firstname="", lastname=""):

    data = ""
    if firstname:
        data = firstname

    else:
        data = lastname

    if re.search(r'[^A-Za-z0-9 ]', data):
        if firstname:
            add_func.print_error_firstname("Firstname format has letters, digits and spaces")
            return
        else:
            add_func.print_error_lastname("Lastname format has letters, digits and spaces")
            return

    return True


def check_phone(phone: str) -> bool or None:

    if (phone.startswith("+7") and len(phone) == 12) or (phone.startswith("8") and len(phone) == 11):
        phone = phone.replace("+7", "8", 1)
    else:
        add_func.print_error_phone("Number format should be like this +7/8XXXXXXXXXXX")
        return

    # патттерн - все кроме цифр
    if re.findall(r"\D", phone):
        add_func.print_error_phone("Number doesn't have letters")
        return

    return True


def check_birthday(birthday: str):

    try:
        # if incorrect date birthday, function time.strptime() raise ValueError
        time.strptime(birthday, '%d.%m.%Y')

        if len(birthday) != 10:
            raise ValueError

    except ValueError:
        add_func.print_error_birthday("Date birthday format should be like this \"DD.MM.YYYY\" and doesn't have letters")
        return

    return True


if __name__ == '__main__':
    add_func.usual_print(check_firstname_or_lastname(firstname="asdeqw"))
    add_func.usual_print(check_phone("89200141489"))
    add_func.usual_print(check_birthday("12.02.2020"))
