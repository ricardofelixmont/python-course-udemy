friends = ['Lucas', 'Carlos', 'Ewerton']

for index, friend in enumerate(friends):   # A função enumerate() retorna um generator
    print(f'{index + 1}° {friend}')


friend_generator = enumerate(friends)

print(next(friend_generator))

# Podemos fazer também:
k, v = next(enumerate(friends))
print(k)
print(v)




k = zip(friends) # Também retorna um iteravel
print(next(k))


ages = [25, 27, 23]

nome_idade = list(zip(friends, ages))
print(nome_idade)

nome, idade = zip(*nome_idade)
print(nome)
print(idade)
