from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta): # Esta é uma classe abstrata em python
    """ Não podemos instanciar essa classe, apenas herdá-la
        Se não sobreescrevermos os métodos abstratos, o seguinte erro vai acontecer:
            
              Traceback (most recent call last):
              File "ABCs_abstract_base_classes.py", line 20, in <module>
              dog = Dog('Rolf')
              TypeError: Can't instantiate abstract class Dog with abstract methods num_legs

"""
    
    def walk(self):
        print('Walking...')

    @abstractmethod
    def num_legs(self): # Assim como no Java sou obrigado a implementar o método na subclass
        pass

    
class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        """ Preciso implementar esse método, caso contrario,
        acontecerá o erro mencionado no __doc__ da superclasse animal
        """
        return 4
    

class Monkey(Animal):
    def __init__(self, name):
        self.name = name

    def num_legs(self):
        return 2


animals = [Dog('Rolf'), Monkey('Bob')]

for a in animals:
    print(isinstance(a, Animal))   # varificando se 'a' é uma instancia da classe abstrata 'Animal'
    print(a.num_legs())


dog = Dog('Rolf')
print(dog.num_legs())

