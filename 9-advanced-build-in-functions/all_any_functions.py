'''
    any() -> recebe um iteravel( por exemplo uma lista) e retorna True se algum dos elementos for avaliado como True
    all() -> recebe um iteravel e retorna True se todos os elementos forem avaliados como True

'''


friends = [
  {
    'name': 'Rolf',
    'location': 'Washington, D.C.'
  },
  {
    'name': 'Anna',
    'location': 'San Francisco'
  },
  {
    'name': 'Charlie',
    'location': 'San Francisco'
  },
  {
    'name': 'Jose',
    'location': 'San Francisco'
  },
]


your_location = input('where are you right now? ')

friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if len(friends_nearby) > 0:
    print('You\'re not alone!')

if any(friends_nearby):          # A função any() verifica cada elemento do iteravel e verifica se ele é avaliado como True com bool(elemento)
                                 # Se pelo ao menos um dos elementos retornar True, ele printa a mensagem
    print('You\'re not alone!')

if all(friends_nearby):
    print('Your\'re not alone!')



'''
* `0`
* `None`
* `[]`
* `()`
* `{}`
* `False`

All other values evaluate to `True`—so if we have a dictionary with values in it, that evaluates to `True` and the `any()` function will then return `True`.

However, if we pass it an empty list, we get `False`.
''' 



# Exemplo do all()

print(all([1,2,3,4,5]))
print(all([0,1,2,3,4]))    # zero é um valor que retorna falso quando bool(0)
