amigos = {'Lucas', 'Ewerton'}
user = set() # dessa forma criamos um conjunto vazio

user.add(str(input('Type a name: ')))

# Se o amigo digitado estiver em amigos, ele retorna o nome. Se não ele retorna: 'set()' conjunto vazio
print(user.intersection(amigos)) # intersecção entre os conjuntos vai retornar se user tem elementos comuns amigos


