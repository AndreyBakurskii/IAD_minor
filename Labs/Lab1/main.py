from json import dump, load
import Labs.Lab1.record as rec


with open("phonebook.json", 'r') as f:
    data = load(f)

    for record in data:
        print(rec.parse_record(record))

