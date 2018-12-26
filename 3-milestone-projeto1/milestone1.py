#!/usr/bin/env python3
# coding: utf-8
# Armazenamento de filmes
# Abaixo temos a lista de dicionários que irá armazenar os filmes:
import os
import csv

# Lista onde são armazendos os filmes em memória
filmes = []

# Abrindo o arquivo csv onde estão armazenados os filmes
with open('filmes.csv', 'r') as arquivo:
    dict_filmes = csv.DictReader(arquivo,delimiter=',')
    for filme in dict_filmes:
        filmes.append(filme)

# Fuções para manipular os filmes
# ADICIONAR UM NOVO FILME
def novo_filme(titulo, ano, diretor='desconhecido'):
    filmes.append({'titulo':titulo, 'ano':ano, 'diretor':diretor})

    with open('filmes.csv', 'a+') as filme:
        fieldnames = ['titulo', 'ano', 'diretor'] # É um parametro obrigatorio do DictWriter(arquivo, fieldnames=fieldnames)  -> este é o cabecalho do arquivo csv
        writer = csv.DictWriter(filme, fieldnames=fieldnames)
        writer.writerow({'titulo': titulo, 'ano': ano, 'diretor':diretor})

    return 'Filme adicionado com sucesso...'

# PROCURAR FILMES PELO ANO
def procurar_filmes_ano(ano):
    lista = []
    for filme in filmes:
        # print(typ(filme['ano'])) # aqui vemos que tudo que vem do dicionario esta vindo como string
        if int(filme['ano']) == ano:
            lista.append(filme)
    return lista

# PROCURAR FILMES PELO TUTULO
def procurar_filmes_titulo(titulo):
    lista = []
    for filme in filmes:
        if filme['titulo'] == titulo:
            lista.append(filme)
    return lista

# PROCURAR FILMES PELO NOME DO DIRETOR
def procurar_filmes_diretor(diretor):
    lista = list()
    for filme in filmes:
        if filme['diretor'] == diretor:
            lista.append(filme)
    return lista

# MOSTRAR TODOS OS FILMES
def mostrar_todos():
    print('LISTA DE FILMES')
    for filme in filmes:
        exibir_filme(filme)


# FUNÇÃO PARA EXIBIR CADA FILME        
def exibir_filme(filme):
    print(f'{"="*7} DADOS DO FILME {"="*7}\nTitulo: {filme["titulo"]}\nAno: {filme["ano"]}\nDiretor: {filme["diretor"]}\n{"="*15}')


# MENU
print('-='*15)
print('MENU')
print('-='*15)

opcao = 0
while opcao not in [6]:
    titulo = ''
    ano = 0
    diretor = ''
    opcao = int(input('[1] - Adicionar novo filme:\n[2] - Pesquisar por titulo:\n[3] - Pesquisar por autor:\n[4] - Mostrar todos:\n[5] - Pesquisar por ano:\n[6] - Sair\nO que você deseja fazer? '))
    os.system('clear')
    if opcao == 6:
        break
    if opcao == 1:
        titulo = str(input('Digite o nome do filme: '))
        ano = int(input('Digite o ano de lançamento: '))
        diretor = str(input('Digite o nome do diretor: '))

        novo_filme(titulo, ano, diretor)
        lista_filmes = procurar_filmes_titulo(titulo)
        for filme in lista_filmes:
            exibir_filme(filme)

    elif opcao == 2:
        titulo = str(input('Digite o nome do filme: '))
        print(titulo)
        lista_filmes = procurar_filmes_titulo(titulo)
        for filme in lista_filmes:
            exibir_filme(filme)


    elif opcao == 3:
        diretor = str(input('Digite o nome do Diretor: '))

        lista_filmes = procurar_filmes_diretor(diretor)
        for filme in lista_filmes:
            exibir_filme(filme)


    elif opcao == 4:
        mostrar_todos()


    elif opcao == 5:
        ano = int(input('Digite o ano de lançamento: '))
        lista_filmes = procurar_filmes_ano(ano)
        for filme in lista_filmes:
            exibir_filme(filme)

    else:
        print('Opção inválida, por favor tente novamente...')
