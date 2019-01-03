#!/usr/bin/env python3.6

""" Um dos principios principais do python é 'ask for forgiveness, not for permission.' """

# Voltando ao exemplo da Garagem

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


class Garage:
    def __init__(self):
        self.cars = list()

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError('Erro: Descrição')
        self.cars.append(car)


ford = Garage()
fiesta = Car('Ford', 'Fiesta')


try:
    ford.add_car(fiesta)

except TypeError: # acontece se uma exceção acontecer.
    print('Your car was not a Car!')


try:
    ford.add_car('Fiesta')
except TypeError: # se um outro tipo de erro acontecer, não vai entrar nesse except e mostrara o erro que
                  # aconteceu
    print('Your car was not a Car!')
    return 0 # mesmo que eu coloque um 'return' dentro do bloco try ou except ou ainda o else, 
             # o finally ainda vai acontecer.
except (ValueError, KeyboardInterrupt):
    print('Tratando uma tupla de erros.')
    raise # utilizamos a palavra reservada raise para que o erro aparece na forma completa, e nao na forma
          # que nós tratamos. Isso é util pois em um programa com muitas linhas de codigo, esse erro
          # tratado pode passar despercebido se houver muitos outros erros. Então isso é muito util quando
          # estamos desenvolvendo. Porém quando o programa estiver pronto é melhor nao deixar o programa
          # parar tao facilmente.
else:
    print('Acontece apenas se não houver uma exceção')
finally:
    print(f'The garage now has {len(ford)} cars.')
# É realmente interessante tratar os erros na interface do usuario. Como no caso acima em que 
# o usuario quer cadastrar um novo carro na garagem. Isso para que o usuario nao veja os 
# tracebacks e as descrições dos erros, isso nao é interessante.



### Considerações sobre erros em python
'''
    Errors can be used to make it explicit when something didn't work as intended, so that the caller can deal with the failure (asking for forgiveness).

Another option, less popular in Python, is to check whether the thing you're trying to do will succeed before doing it (asking for permission).


Python is big on "asking for forgiveness rather than asking for permission". It's baked into the language to use exceptions and exception handling for flow control!
''''



