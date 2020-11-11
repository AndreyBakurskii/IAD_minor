import logging
from prettytable import PrettyTable


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


"""logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("Phone")
logger.error("blablabla")
"""

if __name__ == '__main__':
    pass

# можно создать анонимные функции и там вызывать логгер.ерор с нужным текстом
