from json import dump, load
import Labs.Lab1.record as rec
import Labs.Lab1.phonebook as pb
import Labs.Lab1.additional_functions as add_func

# const variable
CANCEL = "/cancel"
SKIP = ""


def menu():

    menu_str = "Please choose the number command, which you want to execute:\n" \
               "[1] Add new record\n" \
               "[2] Edit a record\n" \
               "[3] Delete a record\n" \
               "[4] Search record\n" \
               "[5] Print phonebook\n" \
               "[6] Exit the program\n"

    print(menu_str)


"""with open("phonebook.json", 'r') as f:
    data = load(f)

    for record in data:
        print(rec.parse_record(record))
"""


def add_new_record(phonebook: pb.Phonebook):

    """
    Ok, you chose to add new record to phonebook. Please, follow instruction.
    """
    check_firstname = False
    check_lastname = False
    check_phone = False
    check_birthday = False

    firstname = ""
    lastname = ""
    phone = ""
    birthday = ""

    while True:

        # checking the data entered by the user
        if not check_firstname:
            data = input("Enter firstname\n"
                         ">>>")

            if data == CANCEL:
                # todo print some farewell
                break

            if rec.check_firstname_or_lastname(firstname=data):
                check_firstname = True
                firstname = data
            else:
                continue

        if not check_lastname:
            data = input("Enter lastname\n"
                         ">>>")

            if data == CANCEL:
                break

            if rec.check_firstname_or_lastname(lastname=data):
                check_lastname = True
                lastname = data
            else:
                continue

        if not check_phone:
            data = input("Enter phone\n"
                         ">>>")

            if data == CANCEL:
                break

            if rec.check_phone(phone=data):
                check_phone = True
                phone = data
            else:
                continue

        if not check_birthday:
            data = input("Enter birthday\n"
                         ">>> ")

            if data == CANCEL:
                break

            if data == SKIP:
                check_birthday = True

            else:
                if rec.check_birthday(data):
                    check_birthday = True
                    birthday = data
                else:
                    continue

        # checking the existence of a similar record
        new_record = rec.Record(firstname=firstname,
                                lastname=lastname,
                                phone=phone,
                                birthday=birthday)

        if pb.check_same_record(phonebook, new_record):
            phonebook.append(new_record)

        else:
            print(
                  "Choose the following way to solve this problem:\n"
                  "[0] Replace existed record in phonebook\n"
                  "[1] Edit firstname of new record\n"
                  "[2] Edit lastname of new record\n"
                  "[3] Edit firstname and lastname of new record\n"
                  "[4] Cancel to add new record",
                  sep="\n"
                  )
            choise = int(input(">>> "))

            if choise == 0:
                phonebook.delete_records(lambda x: x.firstname == new_record.firstname and
                                                   x.lastname == new_record.lastname)
                continue

            if choise == 1:
                check_firstname = False
                continue

            if choise == 2:
                check_lastname = False
                continue

            if choise == 3:
                check_firstname, check_lastname = False, False
                continue

            if choise == 4:
                # todo print some farewell
                break

        return phonebook


def delete_record():
    """
    Ok, you chose to delete some records from phonebook.
    """


if __name__ == '__main__':
    menu()
    phonebook = pb.Phonebook()
    phonebook.append(rec.Record("andrey", "bakur", "89200141489", "30.03.2001"))
    phonebook = add_new_record(phonebook)

    print(phonebook)
