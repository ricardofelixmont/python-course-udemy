variavel = 'hello'
lista = ['hello', 'hi', 'nice to meet you']
tupla = ('hello', 'hi', 'nice to meet you')
set_conjunto = {'hello', 'hi', 'nice to meet you'}

# ESTRUTURA
print(f'Lista: {lista}')
print(f'Tupla: {tupla}')
print(f'Set: {set_conjunto}') # aparece fora de ordem.
# nos testes acima vemos que conjuntos não tem uma ordem especifica, essa ordem pode
# variar de computador para computador.

# TUPLA COM UM ELEMENTO:
# é necessario colocar uma virgula no final para que o python não confunda com parentesis das 
# opeações matematicas.
tupla_unitaria = ('elemento',)
print(tupla_unitaria)
tupla_unitaria2 = 'elemento',
print(tupla_unitaria2)

# ACESSANDO ELEMENTOS
# Listas de tuplas são indexadas, mas sets não.
print(lista[0])
print(tupla[0])
#---
# print(set_conjunto[0]) # Não podemos acessar os elementos dos set dessa forma

# MODIFICANDO AS ESTRUTURAS
lista.append('Eliane')  # isso é possivel pois as listas são mutáveis
print(lista)

# tuplas são imutáveis, portanto não podemos modificar seus elementos(apagar/adicionar)
# para isso precisamos fazer novas tuplas:
# You can create new tuples from existing ones, but you can't append elements to an existing tuple.
tupla = tupla + ('Eliane',)  # Nesse caso fui obrigado a utilizar os parenteses
print(tupla)

# acidionando itens a um conjunto
set_conjunto.add('Eliane')
print(set_conjunto)
set_conjunto.add('hello') # Quando tentamos adicionar itens repetidos nos conjuntos:Não é adicionado
print(set_conjunto)       # Essa é a diferença do set. Ele é uma coleção de elementos únicos.
