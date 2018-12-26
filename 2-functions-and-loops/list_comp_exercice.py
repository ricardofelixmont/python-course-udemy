# Loteria
# Encontrar o jogador com o maior numero de acertos:
# Valor ganho -> winnings = 100 ** len(numbers_matched)

import random
# Criando um conjunto(set) pseudo-aleatoria de 6 numeros no range(22)
lottery_numbers = set(random.sample(list(range(22)), 6))
print(lottery_numbers)

players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]
maior = 0
nome = ''
for player in players:  # player é um dicionario com 'nome' e 'numeros'
    print(player['name'],end=':')
    print(player['numbers'])
    x = player['numbers'] & lottery_numbers
    if len(x) > maior:
        maior = len(x)
        nome = player['name']    

print(f'{nome} ganhou {100**maior}')
    
