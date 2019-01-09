#!/usr/bin/env python3.7
from collections import defaultdict, OrderedDict

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



x = OrderedDict(('Alan' ,'Manchester'),
        ('Bob', 'London'),
        ('Cris', 'Lisbon'),
        ('Dan', 'Paris'),
        ('Eden', 'Liverpool'),
        ('Frank', 'Newcastle')
        )

