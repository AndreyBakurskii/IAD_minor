import re
from prettytable import PrettyTable
import Labs.Lab1.additional_functions as add_func
import time


class Record:

    firstname = "Firstname"
    lastname = "Lastname"
    phone = "Phone"
    birthday = "Birthday"

    def __init__(self, firstname: str, lastname: str, phone: str, birthday=""):
        self.firstname = add_func.do_first_letter_upper(firstname)
        self.lastname = add_func.do_first_letter_upper(lastname)
        self.phone = phone
        self.birthday = birthday

    def __str__(self):
        return f"{self.firstname} | {self.lastname} | {self.phone} | {self.birthday} |"

    def __repr__(self):
        return f"Firstname: {self.firstname}\n" \
               f"Lastname: {self.lastname}\n" \
               f"Phone: {self.phone}\n" \
               f"Birthday: {self.birthday if self.birthday else 'not defined'}\n"

    def conv2dict(self) -> dict:
        return {
                "Firstname":    self.firstname,
                "Lastname":     self.lastname,
                "Phone":        self.phone,
                "Birthday":     self.birthday
                }

    def get_values(self):
        return [self.firstname, self.lastname, self.phone, self.birthday]

    def edit_firstname(self, new_firstname: str):
        self.firstname = add_func.do_first_letter_upper(new_firstname)

    def edit_lastname(self, new_lastname: str):
        self.lastname = add_func.do_first_letter_upper(new_lastname)

    def edit_phone(self, new_phone: str):
        self.phone = new_phone

    def edit_birthday(self, birthday: str):
        self.birthday = birthday


class SetRecords:

    def __init__(self, list_records: list):
        self.list_records = list_records

        # for realize __iter__()
        self.index = 0
        self.length = len(list_records)

    # def get_table(self, index=0, firstname=0, lastname=0, phone=0, birthday=0) -> str:

    def __str__(self):
        table = PrettyTable(["№", "Firstname", "Lastname", "Phone", "Birthday"])
        table.align["№"] = 'l'

        for ind, record in enumerate(self.list_records):

            row = [str(ind)]
            row.extend(record.get_values())

            table.add_row(row)

        return table.get_string()

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.list_records):
            raise StopIteration

        record = self.list_records[self.index]

        self.index += 1

        return record

    def __getitem__(self, index):
        return self.list_records[index] if index < self.length else None


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
    print(check_firstname_or_lastname(firstname="asdeqw"))
    print(check_phone("89200141489"))
    print(check_birthday("12.02.2020"))

    set_ = SetRecords([Record("andrey", "bakurskii", "89200141489"),
                       Record("diana", "utenkova", "89200131389")
                       ])
