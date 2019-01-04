import json

my_json_string = '[{"name":"Alfa Romeo", "released":1950}]'

dicionario = json.loads(my_json_string)
print(dicionario[0]['name'])
