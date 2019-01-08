#!/usr/bin/env python3.7

# Um iterável é todo objeto que possui o método __iter__

class FirstHundredGenerator:   # Generator
    """ Esta é a classe geradora
        Toda classe que possui o método __next__ 
        é um generator e também um iterator
    """
    def __init__(self):
        self.count = 0

    def __next__(self):
        if self.count < 100:
            current = self.count
            self.count += 1

            return current
        else: 
            raise StopIteration()

    def __iter__(self):
        """ Ao inves de criar uma classe separada para isso
        o melhor é sobrescrever esse metodo dentro da classe generator e 
        retornar ele mesmo(objeto generator).
        self é o objeto do tipo 'FirstHundredGenerator' que contem o método __next__.
        """
        return self


g = FirstHundredGenerator()
print(g.__next__())
print(next(g))


'''class FirsHundredIterable:
    """ Este é um iteravel, toda classe que possui o método __iter__ é um iteravel.
        Este método retorna um iterator ou um generator(pois todo generator é um iterator).
        
        Somente com este método é possivel iterar sobre o iterator.
        Vale lembrar que o __getitem__ também faz isso, todo objeto
        que possui o método __getitem__ também é um iterable, porém é usado para strings e listas que aceitam fatiamento e indexação."""
    def __iter__(self):
        return FirstHundredGenerator()


for c in FirsHundredIterable():
    print(c,end=',')
'''
for c in FirstHundredGenerator():
    print(c,end=',')


my_numbers = [x for x in [1 ,2 ,3, 4, 5]]        # Iterable(list)
my_numbers_gen = (x for x in [1, 2, 3, 4, 5])    # Generator

print(next(my_numbers_gen))

# CONSIDERAÇÕES FINAIS:

# ITERATOR: Usado para pegar o proximo valor...
# ITERABLE: usado para iterar sobre todos os valores do iterator.
