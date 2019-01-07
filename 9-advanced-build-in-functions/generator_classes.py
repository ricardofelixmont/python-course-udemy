#!/usr/bin/env python3.7

# A primeira coisa que precisamos ter em mente é que não precisamos do 'yield' em classes generators. Utilizamos 'yield' apenas em funções.

class FirstHundredGenerator:    # Generator/ Iterator
    """ Esta é uma classe generator e seus objetos(instancias) tambem pode ser chamados de iterators"""
    def __init__(self):
        self.number = 0

    def __next__(self):   # Este é o dunder method que nos permite utilizar a função 'next(generator)'
                          # Todos os objetos que possuem esse __next__ method são chamados de 'iterator'
                          # Todos os generators(como essa classe) são iteradores, mas todos os iterators não necessariamente são generators.
        if self.number < 100:
            current = self.number
            self.number += 1
            return current

        else:
            raise StopIteration()    


g = FirstHundredGenerator()    # Iterator -> nem todos os iterators podem ser considerados generators.

print(next(g))

g.__next__()
print(g.number)



# Exemplo de iterator que não é um generator:
# Não estamos retornando valores gerados, estamos retornando valores de uma lista.
class FirstFiveIterator:
    """ Essa é uma classe generator mas seu objeto não é um gererator, é um iterator"""
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0
    
    def __next__(self):  # Quando definimos o metodo __next__ estamos definindo um iterator
        if self.i < len(self.numbers):
            current = self.numbers[self.i]
            self.i += 1
            return current

        else:
            raise StopIteration()


iterator = FirstFiveIterator()
print(next(iterator))


"""
    Uma observação aqui é que os classes acima não permitem iterar sobre seus objetos:
    exemplo:
        g = FirstFiveIterator()
        for number in g:
            print(c)

        Isso não funciona. It will raise an error.    
"""
