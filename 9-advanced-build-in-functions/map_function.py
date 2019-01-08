friends = ['Lucas', 'Carlos', 'Moringa', 'Ewerton']

lower_friends = map(lambda x: x.lower(), friends)
print(lower_friends)  # Retorna um generator object do tipo map e podemos iterar com ele com um loop for
print(next(lower_friends))


# podemos fazer tambem das duas maneiras seguintes:
lower_friends = [x.lower() for x in friends]
print(lower_friends)   # cria um iteravel, no caso uma lista que fica armazenada por completo na memoria.

lower_friends = (c.lower() for c in friends)   # esse é o mais rapido e sempre é melhor usar essa opção do que as outras, isso poupa memoria e muitas vezes processamento.
for f in lower_friends:
    print(f)



# ABAIXO UM EXEMPLO DE SITUAÇÕES ONDE É MELHOR USAR map() do que filter()

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


    @classmethod
    def from_dict(cls, data):
        return data["username"], data["password"]

users = [
    {"username": "rolf", "password":"123"},
    {"username": "Ricardo", "password":"124"}
]

# Podemos separar isso de duas formas:

user = [User.from_dict(u) for u in users]
user = map(User.from_dict, users)  # Nesse caso map() é melhor pois deixa o código muito mais legivel e somente por esse motivo.

