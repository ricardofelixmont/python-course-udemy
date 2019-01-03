nomes = set()
nomes.add(input('Friend1: '))
nomes.add(input('Friend2: '))
nomes.add(input('Friend3: '))

people = open('people.txt')
people_set = set(people.readlines())  # esta escrito dessa forma, por isso na intersecção ele não mostra o resultado correto. 
                                      # {'Lucas Moringa\n', 'Ricardo\n', 'André\n', 'Rafael\n', 'Renata\n', 'Ricardo', 'Ewerton\n', 'Rafael', 'José\n', 'Carlos\n', 'Lucas\n'}

nearby_friends_set = (nomes & people_set) 
print(nearby_friends_set)

for friend in nearby_friends_set:
    print(f'{friend} esta perto')



# como debugar e achar o erro da linha 7. 
# Colocar um breakpoint na linha 7, e depois seguir com o debug devagar até achar a anormalidade.
