#!/usr/bin/env python3

ref_arquivo = open('data.txt') # criando um objeto para armazenar os dados de 'data.txt'
print(type(ref_arquivo))
print(ref_arquivo) 
reader = ref_arquivo.readlines() # Criando uma lista com as linhas do documento 'data.txt'
                                 # cada linha é um item na lista
print(type(reader))
print(reader)

ref_arquivo.close() # fechando o arquivo. Manter arquivos abertos apenas pelo menor tempo possivel.
                    # Apenas o tempo necessário.

# Por exemplo: 
# Manter o arquivo aberto apenas quando necesário.
# Digamos que queremos escrever o nome do usuário:
name = input('Name: ') + '\n'
arquivo = open('data.txt', 'a+')
arquivo.write(name)
arquivo.close()

print(ref_arquivo) #  Apesar de estar fechado ainda consigo ver as informações do objeto.
# reader2 = ref_arquivo.readlines() # Porém não possuo mais suas informações.
# print(reader2)

with open('data.txt', 'r') as f: # Fecha o arquivo automaticamente após a identação
    data = f.readlines()

print(data) # claramente posso usar a variavel(lista) 'data' fora da identação.
