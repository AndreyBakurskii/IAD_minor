import Labs.Lab1.record as rec
import Labs.Lab1.additional_functions as add_func


class Phonebook:

    def __init__(self):
        self.list_records = []

    def __str__(self):
        return str(self.get_records())

    def append(self, record: rec.Record):
        self.list_records.append(record)

    def delete_records(self, comparator=None):
        self.list_records = list(filter(lambda x: True if not comparator(x) else False, self.list_records))

    def get_record(self, comparator=None) -> rec.Record or None:
        for record in self.list_records:
            if comparator(record):
                return record
        return None

    def get_records(self, comparator=None) -> rec.SetRecords or None:
        list_records = list(filter(comparator, self.list_records))

        return rec.SetRecords(list_records) if list_records else None


def check_same_record(phonebook: Phonebook, record: rec.Record) -> True or None:
    comparator = lambda x: x.firstname == record.firstname and x.lastname == record.lastname

    existed_record = phonebook.get_record(comparator)
    if existed_record is not None:
        add_func.print_warning_record("Record with your firstname and lastname has already existed in phonebook.\n" +
                                      "Record: " + str(existed_record) + "\n")
        return

    return True


if __name__ == '__main__':

    phonebook = Phonebook()

    phonebook.append(rec.Record("andrey", "bakur", "89200141489", "30.03.2001"))
    phonebook.append(rec.Record("ivan", "bakur", "89124124124", "15.02.1993"))
    phonebook.append(rec.Record("Diana", "Utenkova", "89564395671", "28.05.2002"))

    print(phonebook.get_records(lambda x: x.firstname == "A"))

    print(phonebook)

