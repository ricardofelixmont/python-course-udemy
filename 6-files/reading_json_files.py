#!/usr/bin/env python3.7
import json


# LENDO UM JSON FILE
with open('json_file.txt', 'r') as f: # Lemos o arquivo como um arquivo de texto comum.
    data = json.load(f)   # Passa o conteudo do json para o objeto 'data' como um dicionario em python.

print(data) # constatamos aqui que temos um dicionario
print(data['friends'][0])  # mostrando o primeiro item da lista de amigos.


# SALVANDO UM JSON FILE
cars = {
        {'make':'Ford', 'model':'Fiesta'},
        {'make':'Ford', 'model':'Focus'}
        }

with open('json_cars.txt', 'w') as f:
    json.dump(cars, f)

""" Como funciona a json.dump(conteudo, arquivo_aberto):
    
    json.dump(dicionario_python, arquivo_onde_quero_guardar)

"""

# também podemos:

arquivo = open('json_cars.txt', 'w')
json.dump(cars, arquivo)

arquivo.close()



# RESUMO: abrimos arquivos json com o a função load() e salvamos com a função dump()



# Podemos também transformar uma string em um dicionario de duas maneiras:
# 1. Utilizando a funçãi json.loads(), o 's' vem da palavra string.
# supondo que temos uma string: 
my_json_string = '[{"name":"Alfa Romeo", "released":1950}]'

dicionario = json.loads(my_json_string)
print(dicionario[0]['name'])


