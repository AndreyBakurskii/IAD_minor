import Labs.Lab1.record as rec


class Phonebook:

    def __init__(self):
        self.list_records = []

    def __str__(self):
        return str(self.get_records())

    def append(self, record: rec.Record):
        self.list_records.append(record)

    def delete_records(self, func=None):
        self.list_records = list(filter(lambda x: True if not func(x) else False, self.list_records))

    def get_records(self, func=None) -> rec.SetRecords:
        return rec.SetRecords(list(filter(func, self.list_records)))


if __name__ == '__main__':

    phonebook = Phonebook()

    phonebook.append(rec.Record("andrey", "bakur", "89200141489", "30.03.2001"))
    phonebook.append(rec.Record("ivan", "bakur", "89124124124", "15.02.1993"))
    phonebook.append(rec.Record("Diana", "Utenkova", "89564395671", "28.05.2002"))

    print(phonebook)

