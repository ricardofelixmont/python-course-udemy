import csv, json

# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:

lista = list()

with open('csv_file_exercice.csv', 'r') as f:
    data = csv.DictReader(f)

    lista = [dict(d) for d in data]

print(lista)

with open('json_file_exercice.txt', 'w') as f:
    json.dump(lista, f)
