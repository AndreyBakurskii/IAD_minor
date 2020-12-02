import messages as ms
import record as rec
import phonebook as pb
import additional_functions as add_func

from json import dump, load
from datetime import date, timedelta


def handle_input_data(func):
    """
    Декотратор для обработки функций для ввода всех видов входных данных: имя, фамилия, номер телефона, дата рождения,
    однозначный и многозначный выборы. Функция возвращает результат работы функции для ввода данных и код ошибки, если
    появилась. У пользователя есть три попытки чтобы ввести корректные данные. Если же пользователь ввел команду отмены
    или пункт отмены в меню, то сразу выводится сообщение об отмене команды. Если пользователь потратил все попытки, то
    выводится сообщения об ошибке и об окончании попоыток ввести данные. Если же пользователь ввел корректные данные,
    то они будут сразу выведены.

    :param func: оборачиваемая декоратором функция - функция для ввода данных
    :return: пара значений: если без ошибок, то (int/str/list, None), иначе (None, int).
    """
    amount_attempts = 3

    def wrap(*args, **kwargs):
        for i in range(amount_attempts):
            res, err = func(*args, **kwargs)

            if err is None:
                return res, err

            if err == ms.CANCEL:
                print(ms.COMMAND_CANCEL, end="\n")
                return None, ms.CANCEL

            if err == ms.SKIP:
                print(ms.COMMAND_SKIP, end="\n")
                return None, ms.SKIP

            add_func.print_error(ms.MESSAGE_OF_ERROR[err])
            print(f"You have {amount_attempts - 1 - i} attempt to enter the data", end="\n")

        print(ms.NOT_HAVE_ATTEMPT)
        return None, ms.END_ATTEMPTS

    return wrap


@handle_input_data
def get_unambiguous_choice(max_number: int) -> (int, None) or (None, int):
    """
    Функция для ввода пользователем однозначного выбора пункта меню. Функция возвращает пару значений - результат работы
    (номер пункта) и код ошибки, если появилась. После ввода, происходит проверка данных по нескольким критериям:
    1. команда отмены ввода данных
    2. наличие не целочисленных данных
    3. проверка на корректный номер пункта, не должен выходить за определенные границы, верхняя граница - входной
    параметр max_number.

    :param max_number: последнее число пункта в меню, который является отменой ввода данных
    :return: пара значений: если без ошибок, то (int, None), иначе (None, int).
    """
    value = input(">>> ")
    try:
        choice = int(value)

        if -1 <= choice < max_number:
            return choice, None

        if choice == max_number:
            return None, ms.CANCEL

        raise ValueError

    except ValueError:
        return None, ms.ERROR_GET_UNAMBIGUOUS_CHOICE


@handle_input_data
def get_multiple_choice(max_number: int) -> (list, None) or (None, int):
    """
    Функция для ввода пользователем многозначного выбора пунктов меню. Функция возвращает пару значений - результат
    работы (список выбранных пунктов) и код ошибки, если появилась. После ввода, происходит проверка данных по
    нескольким критериям:
    1. пункт отмены ввода данных, равный max_number
    2. наличие не целочисленных данных
    3. проверка на корректный номер пункта, не должен выходить за определенные границы, верхняя граница - входной
    параметр max_number.

    :param max_number: последнее число пункта в меню, который является отменой ввода данных
    :return: пара значений: если без ошибок, то (list, None), иначе (None, int).
    """
    values = input(">>> ")
    try:
        choices = list(map(int, values.split()))

        for choice in choices:
            if 0 <= choice < max_number:
                pass
            else:
                raise ValueError

            if choice == max_number:
                return None, ms.CANCEL

        return choices, None

    except ValueError:
        return None, ms.ERROR_GET_MULTIPLE_CHOICE


@handle_input_data
def get_firstname() -> (str, None) or (None, int):
    """
    Функция для ввода пользователем имени. Функция возвращает пару значений -результат работы (имя) и код ошибки,
    если появилась. После ввода, происходит проверка данных по нескольким критериям:
    1. команда отмены ввода данных
    2. проверка на корректность имени, первая буква которого приведена к верхнему регистру

    :return: пара значений: если без ошибок, то (str, None), иначе (None, int).
    """
    print(ms.GET_FIRSTNAME)

    data = input(">>> ")

    if data == ms.CANCEL_STR:
        return None, ms.CANCEL

    res, err = rec.check_firstname_or_lastname(firstname=add_func.do_first_letter_upper(data))

    return res, err


@handle_input_data
def get_lastname() -> (str, None) or (None, int):
    """
    Функция для ввода пользователем фамилии. Функция возвращает пару значений -результат работы (фамилию) и код ошибки,
    если появилась. После ввода, происходит проверка данных по нескольким критериям:
    1. команда отмены ввода данных
    2. проверка на корректность фамилии, первая буква которой приведена к верхнему регистру

    :return: пара значений: если без ошибок, то (str, None), иначе (None, int).
    """
    print(ms.GET_LASTNAME)

    data = input(">>> ")

    if data == ms.CANCEL_STR:
        return None, ms.CANCEL

    res, err = rec.check_firstname_or_lastname(lastname=add_func.do_first_letter_upper(data))

    return res, err


@handle_input_data
def get_phone() -> (str, None) or (None, int):
    """
    Функция для ввода пользователем номера телефона. Функция возвращает пару значений -результат работы (номер телефон в
    строковом виде) и код ошибки, если появилась. После ввода, происходит проверка данных по нескольким критериям:
    1. команда отмены ввода данных
    2. проверка на корректность номера телефона

    :return: пара значений: если без ошибок, то (str, None), иначе (None, int).
    """
    print(ms.GET_PHONE)

    data = input(">>> ")

    if data == ms.CANCEL_STR:
        return None, ms.CANCEL

    res, err = rec.check_phone(data)

    return res, err


@handle_input_data
def get_birthday() -> (str, None) or (None, int):
    """
    Функция для ввода пользователем даты рождения. Функция возвращает пару значений -результат работы (дата рождения в
    строковом виде) и код ошибки, если появилась. После ввода, происходит проверка данных по нескольким критериям:
    1. команда отмены ввода данных
    2. команда пропуска ввода (дата рождения необязательный атрибут записи)
    3. проверка на корректность даты рождения

    :return: пара значений: если без ошибок, то (str, None), иначе (None, int).
    """
    print(ms.GET_BIRTHDAY)

    data = input(">>> ")

    if data == ms.CANCEL_STR:
        return None, ms.CANCEL

    if data == ms.SKIP:
        return None, ms.SKIP

    res, err = rec.check_birthday(data)

    return res, err


@handle_input_data
def get_index(length: int) -> (int, None) or (None, int):
    """
    Функция для ввода пользователем индекса записи. Функция возвращает пару значений - результат работы (номер индекса)
    и код ошибки, если появилась. После ввода, происходит проверка данных по нескольким критериям:
    1. команда отмены ввода данных
    2. наличие не целочисленных данных
    3. проверка на корректный индекс, не должен выходить за определенные границы, верхняя граница - входной параметр
    length.

    :param length: верхняя граница, невключительно (int)
    :return: пара значений: если без ошибок, то (int, None), иначе (None, int).
    """
    print(ms.GET_INDEX)
    value = input(">>> ")

    if value == ms.CANCEL_STR:
        return None, ms.CANCEL

    try:
        index = int(value)

        if 0 <= index < length:
            return index, None

        raise ValueError

    except ValueError:
        return None, ms.ERROR_GET_INDEX


@handle_input_data
def get_indexes(length: int) -> (list, None) or (None, int):
    """
    Функция для ввода пользователем набора индексов записей. Функция возвращает пару значений - результат работы (список
    индексов) и код ошибки, если появилась. После ввода, происходит проверка данных по нескольким критериям:
    1. команда отмены ввода данных
    2. наличие не целочисленных данных
    3. проверка на корректный индекс, не должен выходить за определенные границы, верхняя граница - входной параметр
    length.

    :param length: верхняя граница, невключительно (int)
    :return: пара значений: если без ошибок, то (list, None), иначе (None, int (номер ошибки)).
    """
    print(ms.GET_INDEXES)
    values = input(">>> ")

    if values == ms.CANCEL_STR:
        return None, ms.CANCEL

    try:
        indexes = list(map(int, values.split()))

        for index in indexes:
            if 0 <= index < length:
                continue
            else:
                raise ValueError

        return indexes, None

    except ValueError:
        return None, ms.ERROR_GET_INDEXES


def getting_f_l_name() -> (str, str) or (None, None):
    """
    Функция для объединения функций ввода пользователем имени и фамилии. В случае успешной работы функции возвращается
    данные пользователем имя и фамилия, иначе None, None.

    :return: если без ошибок, то (str, str), иначе (None, None).
    """
    firstname, err = get_firstname()
    if err:
        return None, None

    lastname, err = get_lastname()
    if err:
        return None, None

    return firstname, lastname


def getting_fields() -> rec.Record or None:
    """
    Функция для объединения функций ввода данных соответствующего поля ползователем. В случае успешной работы функции
    возвращается новая запись (rec. None), иначе None.

    :return: если без ошибок, то rec.Record, иначе None.
    """
    firstname, err = get_firstname()
    if err:
        return

    lastname, err = get_lastname()
    if err:
        return

    phone, err = get_phone()
    if err:
        return

    birthday, err = get_birthday()
    if err != ms.SKIP and err is not None:
        return

    new_record = rec.Record(firstname=firstname,
                            lastname=lastname,
                            phone=phone,
                            birthday=birthday)
    return new_record


def select_record(phonebook: pb.Phonebook,
                  multiple_choice=False,
                  index=False,
                  firstname_lastname=False,
                  firstname=False,
                  lastname=False,
                  phone=False,
                  birthday=False) -> rec.SetRecords or None:
    """
    Нахождение набора записей по любому количеству полей. В начале функции составляется меню полей исходя из входных
    параметров, а также добавляются нужные функции для ввода пользователем данных. Затем, согласно выбору пользователя,
    происходит ввод данных и нахождение и вывод нужного набора записей из данной телефонной книги. В случае успешной
    работы функции выводится набор записей (rec.SetRecords), иначе None.

    :param phonebook: данная телефонная книга, в которой происходит поиск нужного набора (pb.Phonebook)
    :param multiple_choice: флаг о типе выбора полей записи пользователем, множественный или однозначный
    (несколько полей или одно), (bool)
    :param index: флаг о выводе индекса в меню выбора (bool)
    :param firstname_lastname: флаг о выводе и имени, и фамилии в меню выбора (bool)
    :param firstname: флаг о выводе только имени в меню выбора (bool)
    :param lastname: флаг о выводе фамилии в меню выбора (bool)
    :param phone: флаг о выводе телефона в меню выбора (bool)
    :param birthday: флаг о выводе даты рожедения в меню выбора (bool)
    :return: если без ошибок, то rec.SetRecords, иначе None
    """
    func_for_input = []
    k = 0
    menu = "You can select a record by the following criteria. "
    if multiple_choice:
        menu += "So, enter number or numbers of field:\n"

    else:
        menu += "So, enter number of field:\n"

    if index:
        menu += f"[{k}] select by index\n"
        func_for_input.append(("index", lambda: get_index(phonebook.get_amount_of_records())))
        k += 1

    if firstname_lastname:
        menu += f"[{k}] select by firstname and lastname\n"
        func_for_input.append(("firstname_lastname", getting_f_l_name))
        k += 1

    if firstname:
        menu += f"[{k}] select by firstname\n"
        func_for_input.append(("firstname", get_firstname))
        k += 1

    if lastname:
        menu += f"[{k}] select by lastname\n"
        func_for_input.append(("lastname", get_lastname))
        k += 1

    if phone:
        menu += f"[{k}] select by phone\n"
        func_for_input.append(("phone", get_phone))
        k += 1

    if birthday:
        menu += f"[{k}] select by birthday\n"
        func_for_input.append(("birthday", get_birthday))
        k += 1

    menu += f"[{k}] cancel\n"

    print(menu)

    if not multiple_choice:
        choice, err = get_unambiguous_choice(k)
        if err:
            return

        field, func = func_for_input[choice]
        if field == "index":
            print(phonebook)

            in_index, err = func()
            if err:
                return

            record = phonebook[in_index]
            if record is None:
                return

            return rec.SetRecords([record])

        if field == "firstname_lastname":
            firstname, lastname = func()
            if firstname is None or lastname is None:
                return

            comparator = f"x.firstname == '{firstname}' and x.lastname == '{lastname}'"
            set_records = phonebook.get_records(comparator=lambda x: eval(comparator))

            if set_records is None:
                return

            return set_records

        data, err = func()
        if err:
            return

        comparator = f"x.{field} == '{data}'"
        set_records = phonebook.get_records(comparator=lambda x: eval(comparator))
        if set_records is None:
            return

        return set_records

    else:
        choices, err = get_multiple_choice(k)
        if err:
            return

        requests = []

        for choice in choices:
            field, func = func_for_input[choice]
            data, err = func()
            if err:
                return

            comparator = f"x.{field} == '{data}'"
            requests.append(comparator)

        set_records = phonebook.get_records(comparator=lambda x: eval(" and ".join(requests)))
        if set_records is None:
            return

        return set_records


def add_new_record(phonebook: pb.Phonebook, new_record: rec.Record) -> pb.Phonebook or None:
    """
    Добавление новой записи в данную телефонную книгу. Функция работает в бесконечном цикле до тех пор, пока не
    выявится ошибка, либо не завершится успешно. В цикле происходит проверка на совпадение с существующей записью в
    данной телефонной книге

    :param phonebook: данная телефонная книга, в которую добавляется новая запись (pb.Phonebook)
    :param new_record: новая запись (rec.Record)
    :return: измененная телефонная книга (pb.Phonebook), либо, в случае какой-либо ошибки, None
    """
    while True:
        if pb.similar_record_in_phonebook(phonebook, new_record):
            print(ms.MENU_TO_SOLVE_SIMILAR_RECORD)
            choice, err = get_unambiguous_choice(2)
            if err:
                return

            if choice == 0:
                phonebook.delete_records(lambda x: x.firstname == new_record.firstname and
                                                   x.lastname == new_record.lastname)

            if choice == 1:
                new_record = edit_record(phonebook, new_record, edit_when_add=True)
                if new_record is None:
                    return
        else:
            phonebook.append(new_record)
            return phonebook


def edit_record(phonebook: pb.Phonebook, record: rec.Record, edit_when_add=False) -> rec.Record or pb.Phonebook or None:
    """
    Редактирование записи. Есть две ветви работы функции.

    Первая - если функция была вызвана из функции добавления записи в телефонную книгу (флаг edit_when_add == True), то
    пользователю предлагается изменить только имя и фамилию, и возвращается отредактированная запись.

    Вторая - если функция была вызвана из главного меню, то пользователю предлагается на выбор
    поле записи, которое он хочет изменить. Если пользователь выбрал имя или фамилию, то предполагаемая запись
    проверяется на совпадение с уже существующей записью в данной телефонной книге. Если запись совпадает с
    существующей, то запускается эта же функция, но уже с флагом edit_when_add. После того как предполагаемся запись
    подходит, то данная запись редактируется. Если пользователь выбрал поле телефон или день рождения, то проверки на
    совпадение предполагаемой  записи не проводится и сразу редактируется данная запись. В результате работы этой ветви
    возвращается измененая телефонная книга.

    :param phonebook: данная телефонная книга (pb.Phonebook)
    :param record: данная запись, которую нужно редактировать (rec.Record)
    :param edit_when_add: флаг для определения работы функции (bool)
    :return: rec.Record если первая ветвь работы, ph.Phonebook, если вторая; если возникла какая-то ошибка то None
    """
    if edit_when_add:

        print(ms.MENU_EDIT_RECORD_WHEN_ADD)

        choice, err = get_unambiguous_choice(3)
        if err:
            return

        if choice == 0:
            firstname, err = get_firstname()
            if err:
                return

            record.edit_firstname(firstname)

        if choice == 1:
            lastname, err = get_lastname()
            if err:
                return

            record.edit_lastname(lastname)

        if choice == 2:
            firstname = get_firstname()
            if err:
                return

            lastname = get_lastname()
            if err:
                return

            record.edit_firstname(firstname)
            record.edit_lastname(lastname)

        return record

    print(repr(record))
    print(ms.MENU_EDIT_RECORD)

    choice, err = get_unambiguous_choice(4)
    if err:
        return

    if choice == 0 or choice == 1:
        edited_record = None

        if choice == 0:
            firstname, err = get_firstname()
            if err:
                return

            edited_record = rec.Record(firstname, record.lastname, record.phone, record.birthday)

        if choice == 1:
            lastname, err = get_lastname()
            if err:
                return

            edited_record = rec.Record(record.firstname, lastname, record.phone, record.birthday)

        while True:
            if pb.similar_record_in_phonebook(phonebook, edited_record):
                edited_record = edit_record(phonebook, edited_record, edit_when_add=True)

                if edited_record is None:
                    return
            else:
                record.edit_firstname(edited_record.firstname)
                record.edit_lastname(edited_record.lastname)
                break

    if choice == 2:
        phone, err = get_phone()
        if err:
            return

        record.edit_phone(phone)

    if choice == 3:
        birthday, err = get_birthday()
        if err:
            return

        record.edit_birthday(birthday)

    return phonebook


def delete_record(phonebook: pb.Phonebook, set_records: rec.SetRecords) -> pb.Phonebook or None:
    """
    Удаление данного набора записей из данной телефонной книги. Перед удалением запрос на согласие действия. Если в
    наборе несколько записей, то предоставляется выбор записей, которые нужно удалить.

    :param phonebook: исходная телефонная книга (pb.Phonebook)
    :param set_records: набор записей для удаления (rec.SetRecords)
    :return: измененная телефонная книга (pb.Phonebook), если функция сработала без ошибок, иначе None
    """
    print(set_records)

    if set_records.length == 1:
        print(ms.MENU_BEFORE_DELETE_RECORD)

        choice_y_n, err = get_unambiguous_choice(1)
        if err:
            return

        if choice_y_n == 0:
            record = set_records[0]
            phonebook.delete_records(lambda x: x.firstname == record.firstname and x.lastname == record.lastname)

    else:

        print(ms.CHOOSE_INDEXES_BEFORE_DELETE_RECORD)

        indexes, err = get_indexes(set_records.length)
        if err:
            return

        print(ms.MENU_BEFORE_DELETE_RECORD)

        choice_y_n, err = get_unambiguous_choice(1)
        if err:
            return

        if choice_y_n == 0:
            for index in indexes:
                phonebook.delete_records(lambda x: x.firstname == set_records[index].firstname and
                                                   x.lastname == set_records[index].lastname)

    return phonebook


def get_age_person(record: rec.Record) -> int or None:
    """
    Получение возраста человека из данной записи.

    :param record: данная запись
    :return: возраст (int), если функция record.get_age() вернула не None, иначе None
    """

    age = record.get_age()
    if age is None:
        return

    return age


def get_persons_birth_within_month(phonebook: pb.Phonebook) -> rec.SetRecords:
    """
    Вывод таблицы с записями, у которых день рождения в ближайший месяц.

    :param phonebook: телефонная книга, в которой происходит поиск нужных записей (pb.Phonebook)
    :return: набор найденых записей (rec.SetRecords)
    """
    records = phonebook.get_records(comparator=None)
    result = []

    today = date.today()
    after_month = today + timedelta(days=30)

    for record in records:
        if record.birthday_date:

            person_date = date(day=record.birthday_date.day, month=record.birthday_date.month, year=today.year)

            if today.year != after_month.year:
                if person_date.month == 1:
                    person_date = date(day=record.birthday_date.day, month=record.birthday_date.month,
                                       year=after_month.year)

            if today <= person_date <= after_month:
                result.append(record)

    return rec.SetRecords(result)


def menu():
    """
    Вывод главного меню.

    :return:
    """
    print(ms.MENU)


def open_phonebook(path2file: str) -> pb.Phonebook:
    """
    Открытие файла, в котором лежит корректная телефонная книга.

    :param path2file: путь к файлу
    :return: объект класса Phonebook, в котором хранится телефонная книга
    """
    with open(path2file, 'r') as file:
        data = load(file)

        return pb.Phonebook([rec.parse_record(record) for record in data])


def save_phonebook(phonebook: pb.Phonebook, path2file: str) -> None:
    """
    Сохранение всех изменений в файл.

    :param phonebook: исходная телефонная книга
    :param path2file: путь к файлу, в который сохранить изменения
    :return: None
    """
    with open(path2file, "w") as file:
        dump(phonebook.conv2json_format(), file, indent=4)


if __name__ == '__main__':
    phonebook = open_phonebook("phonebook.json")

    while True:
        menu()
        choice, err = get_unambiguous_choice(max_number=9)
        if err:
            continue

        # ========= append a new record ==========
        if choice == 1:
            print(ms.APPEND_RECORD_START)
            new_rec = getting_fields()

            if new_rec is None:
                continue

            result = add_new_record(phonebook, new_rec)

            if result is None:
                continue

            phonebook = result

            print(ms.APPEND_RECORD_END)

        # ========= edit a record =============
        elif choice == 2:
            print(ms.EDIT_RECORD_START)

            set_records = select_record(phonebook,
                                        index=True,
                                        firstname_lastname=True)

            if set_records is None:
                continue

            record = set_records[0]
            phonebook = edit_record(phonebook, record)
            if phonebook is None:
                continue

            print(ms.EDIT_RECORD_END)

        # ========== delete a record ===========
        elif choice == 3:
            print(ms.DELETE_RECORD_START)

            set_records = select_record(phonebook,
                                        firstname_lastname=True,
                                        phone=True)

            if set_records is None:
                continue

            result = delete_record(phonebook, set_records)

            if result is None:
                continue

            phonebook = result

            print(ms.DELETE_RECORD_END)

        # ========== search some record ============
        elif choice == 4:
            print(ms.SEARCH_RECORD_START)

            set_records = select_record(phonebook,
                                        multiple_choice=True,
                                        firstname=True,
                                        lastname=True,
                                        phone=True,
                                        birthday=True)

            if set_records is None:
                continue

            print(set_records)

            print(ms.SEARCH_RECORD_END)

        # ========= print phonebook ===========
        elif choice == 5:
            print(phonebook)
            continue

        # ========= get age of person =========
        elif choice == 6:
            print(ms.AGE)
            set_records = select_record(phonebook,
                                        index=True,
                                        firstname_lastname=True)

            if set_records is None:
                continue

            record = set_records[0]
            age = get_age_person(record)
            if age is None:
                continue

            print(repr(record))
            print(f"Age = {age}")

        # ========= get people who have birthday within month ========
        elif choice == 7:
            print(ms.AGE_WITHIN_MONTH)

            set_records = get_persons_birth_within_month(phonebook)
            print(set_records.get_table_with_some_field(firstname=True, lastname=True))

        # ======== exit from program =========
        elif choice == 8:
            print(ms.EXIT)
            break

    save_phonebook(phonebook, "phonebook.json")
