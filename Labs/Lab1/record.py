import re
from prettytable import PrettyTable
import additional_functions as add_func
import messages as ms

import time
from dateutil.relativedelta import relativedelta
from datetime import date


class Record:
    """
    Класс Record представляет собой запись в телефонной книге.

    Атрибуты:
        firstname (str),
        lastname (str),
        phone (str),
        birthday (str),
        birthday_date (date);

    Конструкторы:
        __init__

    Перегруженные методы:
        __str__, __repr__;

    Методы:
        conv2dict,
        get_values,
        get_age,
        edit_firstname,
        edit_lastname,
        edit_phone,
        edit_birthday.

    """
    def __init__(self, firstname: str, lastname: str, phone: str, birthday=""):
        self.firstname = add_func.do_first_letter_upper(firstname)
        self.lastname = add_func.do_first_letter_upper(lastname)
        self.phone = phone
        self.birthday = birthday
        self.birthday_date = parse_birthday(birthday) if birthday else None

    def __str__(self) -> str:
        return f"{self.firstname} | {self.lastname} | {self.phone} | {self.birthday} |"

    def __repr__(self) -> str:
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

    def get_values(self) -> list:
        return [self.firstname, self.lastname, self.phone, self.birthday]

    def get_age(self) -> int or None:
        """
        Получение возраста человека, который отражен в записи. Если дата рождения не определена, выводится ошибка.

        :return: если без ошибок, то int, иначе None.
        """
        today = date.today()
        if self.birthday_date:
            age = relativedelta(today, self.birthday_date)

            return age.years
        else:
            add_func.print_error(ms.MESSAGE_OF_ERROR[ms.ERROR_NOT_BIRTHDAY])
            return

    def edit_firstname(self, new_firstname: str):
        self.firstname = add_func.do_first_letter_upper(new_firstname)

    def edit_lastname(self, new_lastname: str):
        self.lastname = add_func.do_first_letter_upper(new_lastname)

    def edit_phone(self, new_phone: str):
        self.phone = new_phone

    def edit_birthday(self, new_birthday: str):
        self.birthday_date = parse_birthday(new_birthday)
        self.birthday = new_birthday


class SetRecords:
    """
    Класс SetRecords представляет собой набор записей. Класс создан для возвращения нескольких записей, их вывода и
    итерирования по ним.

    Конструкторы:
        __init__;

    Перегруженные методы:
        __str__, __iter__, __next__, __getitem__;

    Методы:
        get_table_with_some_field;

    """

    def __init__(self, list_records: list):
        self.list_records = list_records

        # for realize __iter__()
        self.index = 0
        self.length = len(list_records)

    def __str__(self) -> str:
        return self.get_table_with_some_field(all_fields=True)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self) -> Record:
        if self.index == len(self.list_records):
            raise StopIteration

        record = self.list_records[self.index]

        self.index += 1

        return record

    def __getitem__(self, index) -> Record or None:
        if index < self.length:
            return self.list_records[index]

        add_func.print_error(ms.MESSAGE_OF_ERROR[ms.ERROR_NOT_EXISTED_RECORD])
        return

    # def append_record(self, record: Record):
    #     self.list_records.append(record)
    #     self.length += 1

    def get_table_with_some_field(self, all_fields=False, firstname=False, lastname=False, phone=False, birthday=False)\
            -> str:
        """
        Реализация строкового представления набора записей. Реализовано с помощью сторонней библиотеки PrettyTable, в
        которой есть одноименный класс, принимающий названия столбцов создаваемой таблицы.
        Данная функция принимает флаги каждого поля записи, но есть флаг all_fields, который означает, что все поля
        записи должны быть выведены в таблице представления.

        :param all_fields: флаг, означающий, что в таблице должны быть все столбцы (поля)
        :param firstname: флаг, означающий, что в таблице должен быть столбец с именами
        :param lastname: флаг, означающий, что в таблице должен быть столбец с фамилиями
        :param phone: флаг, означающий, что в таблице должен быть столбец с номером телефона
        :param birthday: флаг, означающий, что в таблице должен быть столбец с датой рождения
        :return: искомая таблица в строковом виде (str)
        """
        columns = ["№"]
        if all_fields:
            columns.extend(["Firstname", "Lastname", "Phone", "Birthday"])
        else:
            if firstname:
                columns.append("Firstname")
            if lastname:
                columns.append("Lastname")
            if phone:
                columns.append("Phone")
            if birthday:
                columns.append("Birthday")

        table = PrettyTable(columns)
        table.align["№"] = 'l'

        for ind, record in enumerate(self.list_records):
            row = [str(ind)]
            if all_fields:
                row.extend(record.get_values())
            else:
                if firstname:
                    row.append(record.firstname)
                if lastname:
                    row.append(record.lastname)
                if phone:
                    row.append(record.phone)
                if birthday:
                    row.append(record.birthday)

            table.add_row(row)

        return table.get_string()


def parse_birthday(birthday) -> date:
    """
    Парсер даты рождения, на вход принимается дата рождения в строковом виде и конвертируется в объкт класса date
    :param birthday: строковое представление даты рождения ("dd.mm.yyyy")
    :return: объект класса date с распарсерными данными
    """
    day, month, year = list(map(int, birthday.split(".")))

    return date(year=year, month=month, day=day)


def parse_record(data: dict) -> Record:
    """
    Парсер записи из словаря, в котором ключи являются названия полей, а значения - данные этих полей.

    :param data: запись в виде словаря (dict)
    :return: объект класса Record с распарсерными данными
    """
    firstname, lastname, phone, birthday = data.values()

    return Record(firstname, lastname, phone, birthday=birthday)


def check_firstname_or_lastname(firstname="", lastname="") -> (str, None) or (None, int):
    """
    Проверка имени или фамилии в зависимости от входных данных. Проверка происходит с помощью регулярных выражений.
    Паттерны составлены согласно данным условиями. Функция возвращает пару значений - исходная значение и код ошибки,
    если возникла.

    :param firstname: предполагаемое имя новой записи (str)
    :param lastname: предполагаемая фамилия новой записи (str)
    :return: если без ошибок, то (str, None), иначе (None, int).
    """
    data = ""
    if firstname:
        data = firstname

    else:
        data = lastname
    if re.search(r'[^A-Za-z0-9 ]', data):
        if firstname:

            return None, ms.ERROR_FORMAT_FIRSTNAME
        else:
            return None, ms.ERROR_FORMAT_LASTNAME

    return data, None


def check_phone(phone: str) -> (str, None) or (None, int):
    """
    Проверка номера телефона в зависимости от входных данных. Проверка происходит с помощью регулярных выражений.
    Паттерны составлены согласно данным условиями. Функция возвращает пару значений - исходное значение и код ошибки,
    если возникла.

    :param phone: предполагаемый номер телефона новой записи (str)
    :return: если без ошибок, то (str, None), иначе (None, int).
    """

    if (phone.startswith("+7") and len(phone) == 12) or (phone.startswith("8") and len(phone) == 11):
        phone = phone.replace("+7", "8", 1)
    else:
        return None, ms.ERROR_FORMAT_PHONE

    # патттерн - все кроме цифр
    if re.findall(r"\D", phone):
        return None, ms.ERROR_FORMAT_PHONE

    return phone, None


def check_birthday(birthday: str) -> (str, None) or (None, int):
    """
    Проверка даты рождения в зависимости от входных данных. Проверка происходит с помощью регулярных выражений.
    Паттерны составлены согласно данным условиями. Также происходит проверка на рельность даты, то есть если дата позже
    сегодняшней, то выводится соответвствующая ошибка. Функция возвращает пару значений - исходное значение и код
    ошибки, если возникла.

    :param birthday: предполагаемая дата рождение новой записи (str)
    :return: если без ошибок, то (str, None), иначе (None, int).
    """

    try:
        # if incorrect date birthday, function time.strptime() raise ValueError
        time.strptime(birthday, '%d.%m.%Y')
        bth = parse_birthday(birthday)

        if bth > date.today():
            raise ValueError

        if len(birthday) != 10:
            raise ValueError

    except ValueError:
        return None, ms.ERROR_FORMAT_BIRTHDAY

    return birthday, None


# пустая таблица со всеми столбцами
emptyTable = PrettyTable(["№", "Firstname", "Lastname", "Phone", "Birthday"]).get_string()
