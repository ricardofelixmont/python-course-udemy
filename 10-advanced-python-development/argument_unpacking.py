#!/usr/bin/env python3.7


accounts = {
    'checking':1958.00,
    'savings':3695.50
}


def add_balance(amount: float, name: str = 'checking') -> float: 
    """Função que recebe um valor e retorna o novo saldo."""
    accounts[name] += amount
    return accounts[name]


transactions = [
    (-180.67, 'checking'),
    (-110.12, 'savings'),
    (-100.17, 'checking'),
    (150.04, 'savings'),
    (-12.47, 'checking'),
]

# Se quisermos passar cada uma das tuplas pela função 'add_balance':
for t in transactions:
    add_balance(t[0], t[1])

# Porém é mais facil utilizar o * (operador de unpack):
for t in transactions:
    add_balance(*t)  # *t -> x, y = *t separa os valores de t em duas variaveis




# ARGUMENTOS COM NOMES: 
for t in transactions:
    add_balance(amount=t[0], name=t[1])

# Dessa forma nao preciso colocar os argumentos na ordem certa:
for t in transactions:
    add_balance(name=t[1], amount=t[0])




# Bom uso de unpacking:
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])

users = [
    {'username':'rolf', 'password':'123'},
    {'username':'ricardo', 'password':'124'}
]

# Queremos criar objetos do tipo User:
user_objects = map(User.from_dict, users)
# podemos usar ums list comprehension
user_objects = [User.from_dict(user) for user in users]



# Não precisamos do método from_dict, podemos fazer os seguinte:
user_objects = [User(data['username'], data['password']) for data in users]

# Ainda podemos fazer melhor ainda:
user_objects = [User(**data) for data in users]   # ** é o operador de 'dictionary unpack', a partir do python 3 ele retorna os itens do dicionario em ordem.
# Ele faz  o seguinte data['username'], data['password']

