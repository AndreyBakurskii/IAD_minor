import record as rec
import additional_functions as add_func
import messages as ms


class Phonebook:
    """
    Класс Phonebook представляет собой телефонную книгу, которая хранит записи (Record).

    Атрибуты:
        _list_records,
        _amount_of_records;

    Конструкторы:
        __init__;

    Перегруженные методы:
        __str__, __getitem__;

    Методы:
        append,
        delete_records,
        get_record,
        get_records,
        get_amount_of_records,
        conv2json_format;

    """

    def __init__(self, list_records: list):
        self._list_records = list_records

        self._amount_of_records = len(list_records)

    def __str__(self):
        """
        Строковое предствление телефонной книги является строковым представлением набора записей (rec.SetRecords).
        Этот набор возвращается из метода get_records в который ничего не передается, чтобы вернулся полный или пустой
        набор записей, если телефонная книга пуста.

        :return: строковое представление набора записей телефонной записи (str)
        """
        set_records = self.get_records()
        return str(set_records) if set_records else rec.emptyTable

    def __getitem__(self, item: int):
        """
        Получение записи по индексу. В случае отсутствия записи по данному индексу, вывод ошибки и возвращение None.

        :param item: индекс (int)
        :return: искомая запись (rec.Record), либо None
        """
        if item < self._amount_of_records:
            return self._list_records[item]

        add_func.print_error(ms.MESSAGE_OF_ERROR[ms.ERROR_NOT_EXISTED_RECORD])
        return

    def append(self, record: rec.Record):
        """
        Добавление новой записи в телефонную книгу и увелечение счетчика количества записей.

        :param record: новая корректная запись (rec.Record)
        :return:
        """
        self._list_records.append(record)
        self._amount_of_records += 1

    def delete_records(self, comparator=None):
        """
        Удаление записей, которые удовлетворяют компоратору, который передается в функцию. Удаление происходит путем
        обновления списка записей с помощью функции filter(). После удаления обновление счетчика количества записей.

        :param comparator: функция компоратор, согласно которой удаляются записи
        :return:
        """
        self._list_records = list(filter(lambda x: True if not comparator(x) else False, self._list_records))
        self._amount_of_records = len(self._list_records)

    def get_record(self, print_error=True, comparator=None) -> rec.Record or None:
        """
        Получение первой записи, которая удовлетворяет компоратору. Если такой записи нет, то выводится ошибка, если
        флаг print_error равен True,  и возвращается None.

        :param print_error: флаг о выводе ошибки или нет
        :param comparator: функция компоратор, которой должна удовлетворять запись
        :return: если без ошибок, то rec.Record, иначе None.
        """
        for record in self._list_records:
            if comparator(record):
                return record

        if print_error:
            add_func.print_error(ms.MESSAGE_OF_ERROR[ms.ERROR_NOT_EXISTED_RECORD])
        return

    def get_records(self, print_error=True, comparator=None) -> rec.SetRecords or None:
        """
        Получение списка записей, которые удовлетворяют компоратору. Если таких записей нет, то выводится ошибка, если
        флаг print_error равен True, и возвращается None.

        :param print_error: флаг о выводе ошибки или нет
        :param comparator: функция компоратор, которой должны удовлетворять записи
        :return: если без ошибок, то list, иначе None.
        """
        list_records = list(filter(comparator, self._list_records))

        if list_records:
            return rec.SetRecords(list_records)

        if print_error:
            add_func.print_error(ms.MESSAGE_OF_ERROR[ms.ERROR_NOT_EXISTED_RECORD])
        return

    def get_amount_of_records(self):
        """
        Получение количества записей в телефонной книге.

        :return: количество записей (int)
        """
        return self._amount_of_records

    def conv2json_format(self):
        """
        Конвертация объекта класса в формат для кодирования в JSON файл.

        :return: список отконвертируемых в словарь записей (list)
        """
        return [record.conv2dict() for record in self._list_records]


def similar_record_in_phonebook(phonebook: Phonebook, record: rec.Record) -> True or None:
    """
    Проверка существование похожей записи в телефонной книге. Если существует, то выведится предупреждение о
    существовании подобной записи с ее данными.

    :param phonebook: данная телефонная книга в которой происходит проверка
    :param record: запись которая сравнивается с существующимеся в данной телефонной книге записями
    :return: True, если существует подобная запись, иначе None.
    """
    comparator = lambda x: x.firstname == record.firstname and x.lastname == record.lastname

    existed_record = phonebook.get_record(print_error=False, comparator=comparator)
    if existed_record is not None:
        add_func.print_warning(ms.WARNING_EXISTED_RECORD + str(existed_record))
        return True

    return
