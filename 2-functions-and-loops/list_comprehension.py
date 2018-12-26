# Return a double of a list

lista = list(range(10))
#=============================
lista_dobro = list()
print(lista_dobro) # It must show a void list

for num in lista:
    lista_dobro.append(num*2)
print(lista_dobro)
#=============================

# LIST COMPREHENSION WITH LIST
print([num*2 for num in lista])

# We can format strings into a list comprehension:
frases = ['{} anos de idade'.format(num) for num in lista_dobro]
print(frases)

# We can do the same thing with f strings:
frases2 = [f'{num} anos de idade' for num in lista_dobro]
print(frases2)

# Names list
names_list = ['Lucas', 'João', 'Bruno', 'Otávio']
nomes_minusculas = [name.lower() for name in names_list]
print(nomes_minusculas)
nome1 = 'Lucas_Alberto'
nome2 = 'lucas_alberto'
print(nome1.lower())
print(nome2.capitalize())
print(nome2.upper())
print('_'.join([nome.capitalize() for nome in nome2.split('_')])) # Para fazer o capitalize em nomes separados por
                                                                  # algum simbolo.

# Creating a list of even numbers(numeros pares)
print([number for number in range(20) if number % 2 == 0])


# Com as listas 'frinds' e 'guests' construir uma lista com os amigos que vao a festa(que estao entre os convidados)
friends = ['rolf', 'anna', 'charlie']
guests = ['Jose', 'Rolf', 'Charlie', 'michael']
# Meu jeito
guests_friends = [friend for friend in friends if friend.capitalize() in guests]
print(guests_friends)
# Jeito do Professor
present_friends =  [friend for friend in guests if friend.lower() in friends]
print(present_friends)



# LIST COMPREHENSION WITH SETS
friends = {'rolf', 'anna', 'charlie'}
guests = {'jose', 'rolf', 'charlie', 'michael'}

present_friends = {name.capitalize() for name in friends if name in guests}
print(present_friends)
# existe uma maneira melhor de fazer isso:
# utilizando interseção:
friends_intersection = friends & guests
# tambem podemos fazer:
friends_intersection2 = {name.capitalize() for name in friends & guests}
print(friends_intersection)  # pode vir fora de ordem
print(friends_intersection2) # pode vir fora de ordem 



# LIST COMPREHENSION WITH DICTIONARIES

names = ['Rolf', 'Anna', 'Charlie']
time_last_seen = [10, 15, 8]

# Constuir com as listas acima, o seguinte dicionario: {'Rolf':10, 'Anna':15, 'Charlie':8}
# Com list comprehension
print({names[i]:time_last_seen[i] for i in range(len(names))})
# Com zip()
print(dict(zip(names, time_last_seen)))
