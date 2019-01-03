# reading the lines in the file:
import csv


# Lendo como arquivo de texto comum:
with open('csv_file.csv', 'r') as csv_file:
    data = csv_file.readlines()

for line in data:
    print(line.strip().split(','))



print('\n')
# Lendo como arquivo csv, utilizando a biblioteca csv com o método csv.reader(objeto_arquivo)
with open('csv_file.csv', 'r') as f:
    reader = csv.reader(f)  # método csv.reader()
    for c in reader:
        print(c)

print('\n')
# Lendo como arquivo csv, porém dessa vez lendo como DictReader(objeto_arquivo)...a primeira linha é utilizada como chave de cada colunas.
with open('csv_file.csv', 'r') as f:
    dict_reader = csv.DictReader(f)
    linhas = [dict(line) for line in dict_reader]

print(linhas,end='\n'*2)
# criado uma lista com os itens da coluna idade:
[print(linha['nome'].capitalize()) for linha in linhas]
print('\n')

# jutando aquivos com ',':
csv_string = ','.join(['rolf', '25', 'mit'])
print(csv_string,end='\n'*2)




# Um overview sobre formatação de textos:
x = 'shrek_silva nogueira ramalho'
print(x.title()) # a primeira letra de cada palavra do nome se torna maiuscula, mesmo que o separador seja underscore ou um outro qualquer.
print(x.capitalize()) # a primeira letra da string se torna maiuscula.
print(x.upper())
print(x.lower())
