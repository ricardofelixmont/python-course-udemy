# FOR LOOP AND ENUMERATE()
list_ages = [12,13,15,14,16,17]
# for loop in python is just like a for-each in java.
for pos,age in enumerate(list_ages):
    print(f'The {pos+1}° person is {age} years old')

# THE range() function is a generator in python
# so we can usar for loop with that
for number in range(0,10):
    print(number,end='; ')

# For loop with dictionaries:
friends = {'Ewerton':30,'Lucas':25,'Carlos':25}
print('\n')
for chave,valor in friends.items():
    print(chave, valor)

# COMPREHENSION LIST, it has the same output.
[print(chave, valor) for chave,valor in friends.items()]

print(friends.items()) # dict_items([('Ewerton', 30), ('Lucas', 25), ('Carlos', 25)])
                       # o que ele imprime aqui é chamado de 'view' in python(pesquisar), é uma lista de tuplas.

# Using the same dict above
# O python entende que cada item da tupla pode ser extraido para um variavel diferente:
for t in friends.items():
    x, y = t
    print(x)
    print(y)

for name, age in friends.items():
    if name == 'Lucas':
        print(f'Eu conheço o {name}')

# I can also do:
who_do_i_know = 'Ewerton'
if who_do_i_know in friends:
    print(f'Eu também conheço {who_do_i_know}')
