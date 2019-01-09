#!/usr/bin/env python3.7
from collections import defaultdict, OrderedDict, namedtuple, deque

# Tarefa 1
def task1():
    """
    - create a `defaultdict` object, and its default value would be set to the string `Unknown`.
    - Add an entry with key name `Alan` and its value being `Manchester`.
    - Return the `defaultdict` object you created.
    """
    default_dict = defaultdict(lambda: 'Unknown')
    default_dict['Alan'] = 'Manchester' 
    return default_dict

print(task1())

# Tarefa2
def task2(arg_od):
    """
    - takes in an OrderedDict `arg_od`
    - Remove the first and last entry in `arg_od`.
    - Move the entry with key name `Bob` to the end of `arg_od`.
    - Move the entry with key name `Dan` to the start of `arg_od`.
    - You may assume that `arg_od` would always contain the keys `Bob` and `Dan`,
        and they won't be the first or last entry initially.
    """
    arg_od.popitem(last=False)   
    arg_od.popitem(last=True)     # por defaul ja é True -> arg_od.popitem()
    arg_od.move_to_end('Bob')
    arg_od.move_to_end('Dan', last=False)
    return 'Success...'

x = OrderedDict([
        ('Alan' ,'Manchester'),
        ('Bob', 'London'),
        ('Cris', 'Lisbon'),
        ('Dan', 'Paris'),
        ('Eden', 'Liverpool'),
        ('Frank', 'Newcastle')
        ])

task2(x)
print(x)

# Tarefa3
def task3(name, club):
    """
    - create a `namedtuple` with type `Player`, and it will have two fields, `name` and `club`.
    - create a `Player` `namedtuple` instance that has the `name` and `club` field set by the given arguments.
    - return the `Player` `namedtuple` instance you created.
    """
    Player = namedtuple('Player', ['name', 'club'])
    return Player(name, club)

y = task3('Ricardo', 'Real Madrid')
print(y)

Dados = namedtuple('Dados', ['nome', 'sexo']) # cria uma subclasse de tuple()
d = Dados('Dan', 'Masc')    # Instanciou um objeto do tipo 'Dados' -> namedtuple()
print(d)


# Tarefa4
def task4(arg_deque: deque):
    # Deque = double ended queue, é uma lista mais rápida, que permite a entrada de dados tanto no final quanto no começo.
    """
    - Manipulate the `arg_deque` in any order you preferred to achieve the following effect:
        -- remove last element in `deque`
        -- move the fist (left most) element to the end (right most)
        -- add an element `Zack`, a string, to the start (left)
    """
    arg_deque.pop() # Remove the last element
    # Movendo o primeiro elemento para o ultimo lugar da fila:
    arg_deque.append(arg_deque.popleft())
    arg_deque.appendleft('Zack')  

print('task4')
novo_deque = deque(['Carlos', 'Lucas', 'João', 'Bruno'])
task4(novo_deque)
print(novo_deque)




fila_double_ended = deque(['Ricardo', 'Érika'])
print(fila_double_ended)
fila_double_ended.appendleft('Vicência')
print(fila_double_ended)
fila_double_ended.append('Felix')
print(fila_double_ended)

# Removendo o primeiro elemento e jogando para o ultimo lugar da fila:
primeiro_elemento = fila_double_ended.popleft()
fila_double_ended.append(primeiro_elemento)
print(fila_double_ended)


