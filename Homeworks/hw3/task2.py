import os


# format path: d:\python_project\IAD_minor
def gen_for_files(path: str):

    list_elements = os.listdir(path)

    for elem in list_elements:

        elem_path = f"{path}\{elem}"

        if os.path.isfile(elem_path):
            yield elem_path

        else:
            yield from gen_for_files(elem_path)

TEST_PATH = "D:\python_project\IAD_minor\Homeworks"

for elem in gen_for_files(path=TEST_PATH):
    print(elem)
