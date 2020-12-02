# ====== номера ошибок =======

CANCEL = -1

CANCEL_STR = "/cancel"

SKIP = ""

END_ATTEMPTS = 1

ERROR_FORMAT_FIRSTNAME = 10
ERROR_FORMAT_LASTNAME = 11
ERROR_FORMAT_PHONE = 12
ERROR_FORMAT_BIRTHDAY = 13

ERROR_GET_UNAMBIGUOUS_CHOICE = 14
ERROR_GET_MULTIPLE_CHOICE = 15

ERROR_GET_INDEX = 16
ERROR_GET_INDEXES = 17

ERROR_NOT_EXISTED_RECORD = 18

ERROR_NOT_BIRTHDAY = 19

# ========= словарь текстов ошибок ===========

MESSAGE_OF_ERROR = {ERROR_FORMAT_FIRSTNAME: "FIRSTNAME :: Firstname format has letters, digits and spaces",

                    ERROR_FORMAT_LASTNAME: "LASTNAME :: Lastname format has letters, digits and spaces",

                    ERROR_FORMAT_PHONE: "PHONE :: Number format should be like this +7/8XXXXXXXXXXX and "
                                        "doesn't have letters",

                    ERROR_FORMAT_BIRTHDAY: "BIRTHDAY :: Date birthday format should be like this "
                                           "\"DD.MM.YYYY\", doesn't have letters and be real data",

                    ERROR_GET_UNAMBIGUOUS_CHOICE: "CHOICE :: Choice is number of commands, which are provided,"
                                                  " not letters and etc.",

                    ERROR_GET_MULTIPLE_CHOICE: "CHOICE :: Multiple choices consist of numbers of commands, which are "
                                               "provided, and separated by space",

                    ERROR_GET_INDEX: "INDEX :: Index must be number, which is in the set",

                    ERROR_GET_INDEXES: "INDEX :: Indexes must be numbers, which are in the set, and separated by space",

                    ERROR_NOT_EXISTED_RECORD: "RECORD :: Phonebook or set records doesn't have this record",

                    ERROR_NOT_BIRTHDAY: "RECORD :: This record doesn't have birthday",
                    }

# ====== предупреждения ==========

WARNING_EXISTED_RECORD = "RECORD :: Record with your firstname and lastname has already existed in phonebook.\n" \
                         "Record: "

# ======= различные сообщения пользователю в консоль ==========

GET_FIRSTNAME = "\nEnter firstname, please. Firstname format has letters, digits and spaces, " \
                "if you change your mind enter '/cancel'"

GET_LASTNAME = "\nEnter lastname, please. Lastname format has letters, digits and spaces, " \
               "if you change your mind enter '/cancel'"

GET_PHONE = "\nEnter phone, please. Phone format should be like this +7/8XXXXXXXXXXX and doesn't have letters, " \
            "if you change your mind enter '/cancel'"

GET_BIRTHDAY = "\nEnter birthday, please. Date birthday format should be like this \"DD.MM.YYYY\" and doesn't have " \
               "letters, if you change your mind enter '/cancel'"

GET_INDEX = "\nEnter index of record from table" \
            " if you change your mind enter '/cancel'"

GET_INDEXES = "\nEnter indexes of records from table separated by space" \
              " if you change your mind enter '/cancel'"

COMMAND_CANCEL = f"Command canceled!"

COMMAND_SKIP = f"Command skipped!"

NOT_HAVE_ATTEMPT = f"You don't have attempts to enter data"


APPEND_RECORD_START = "You choose to append a new record to phonebook. Please, follow instructions.\n"
APPEND_RECORD_END = "The new record was appended successfully\n"

EDIT_RECORD_START = "You choose to edit some record from phonebook. Please, follow instructions.\n"
EDIT_RECORD_END = "The record was edited successfully!\n"

SEARCH_RECORD_START = "You choose to search some record from phonebook. Please, follow instructions.\n"
SEARCH_RECORD_END = "The command to search a record was executed successfully\n"

DELETE_RECORD_START = "You choose to delete a record from phonebook. Please, follow instructions.\n"
CHOOSE_INDEXES_BEFORE_DELETE_RECORD = "What records do you want to delete from phonebook?\n"
DELETE_RECORD_END = "Deletion was successful"

AGE_WITHIN_MONTH = "You choose to search some people, which have birthday within month. Please follow instructions.\n"

AGE = "You choose to get age of some person from phonebook. Please, follow instructions\n"

EXIT = "Thanks for using that program. All changes will save, don't worry! Bye-Bye!"


# ======== каждое меню с пунктами =========

MENU = "\nPlease choose the number command, which you want to execute:\n" \
       "[1] Add new record\n" \
       "[2] Edit a record\n" \
       "[3] Delete a record\n" \
       "[4] Search records by any field or multiple fields\n" \
       "[5] Print phonebook\n" \
       "[6] Get age person\n" \
       "[7] Get records of people who have a birthday within a month\n" \
       "[8] Exit the program\n"

MENU_TO_SOLVE_SIMILAR_RECORD = "Choose the following way to solve this problem:\n" \
                               "[0] Replace existed record in phonebook\n" \
                               "[1] Edit a new record\n" \
                               "[2] Cancel to add new record\n"

MENU_EDIT_RECORD_WHEN_ADD = "What field do you want to edit? Enter number of field:\n" \
                            "[0] Edit firstname of new record\n" \
                            "[1] Edit lastname of new record\n" \
                            "[2] Edit firstname and lastname of new record\n" \
                            "[3] Cancel edit a new record\n"

MENU_EDIT_RECORD = "What field do you want to edit? Enter number of field:\n" \
                   "[0] Firstname\n" \
                   "[1] Lastname\n" \
                   "[2] Phone\n" \
                   "[3] Birthday\n" \
                   "[4] Cancel to edit record\n"

MENU_BEFORE_DELETE_RECORD = "Are you sure you want to delete this record?\n" \
                            "Enter your answer:\n" \
                            "[0] YES\n" \
                            "[1] Cancel this command and return to main menu\n"



