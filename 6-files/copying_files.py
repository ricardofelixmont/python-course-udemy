# ask the user for a list of 3 friends
# for each friend, we'll tell the user whether they are nearby
# for each nearby friend, we'll save their name to 'nearby_friends.txt'

friends = list()
friends.append(input('Friend1: '))
friends.append(input('Friend2: '))
friends.append(input('Friend3: '))
friends = list(set(friends))  # Faço casting para set() para que ele não possua valores repetidos.
                              # E então faço casting para list() novamente.
print(friends)
print(type(friends))

with open('people.txt', 'r') as f:
    pessoas = f.readlines()

texto = ''
for friend in friends:
    for pessoa in pessoas:
        if friend.strip() == pessoa.strip():
            texto += friend + '\n'

ref_arquivo = open('nearby_friends.txt', 'a+')
ref_arquivo.write(texto)
ref_arquivo.close()

# podemos fazer também com sets. Isso removeria nomes duplicados automaticamente.
