dicionario = [{"Nome": "Elias"},{"Nome":"Carlos"}, {"Nome":"Cassandra"}]
del dicionario[0]["Nome"] # apagando o par chave valor do dicionario do primeiro indice da lista.
print(dicionario) # aqui vemos que ele fica como um dicionario, mais precisamente um set {} vazio na lista.


# REMOVENDO ITENS DE UMA LISTA
lista = [1,2,3,4,5,6,7]
print(lista.pop(3)) # Remove pelo indice lista.pop(indice) e retorna o valor removido
# podemos fazer:  x = lista.pop(3), no caso x = 4
print(lista)

lista.remove(3) # vai remover o primeiro numero 3 que ele encontrar
print(lista)

del lista[1]  # tambem remove pelo indice
print(lista)


