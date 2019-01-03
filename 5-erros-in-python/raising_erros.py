#!/usr/bin/env python3.6

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car{self.make} {self.model}'



class Garage:
    def __init__(self):
        self.cars = list()

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        """ A exceção abaixo vai acontecer se tentarmos adicionar um carro 
            dentro da garagem
        """
        raise NotImplementedError('Não podemos adicionar carros a garagem ainda.')
    
    def add_car2(self, car):
        """ Digamos que queremos adicionar na lista apenas objetos do tipo Car.
            Podemos fazer isso graças a uma built-in function no python chamada 'isinstance'.
            sintaxe: isinstance(objeto, Classe), verifica se o objeto é do tipo da Classe.
        """
        if not isinstance(car, Car):
            raise TypeError(f'Você tentou adicionar um `{car.__class__.__name__}` a garagem, mas você só pode adicionar objetos do tipo Car')
        self.cars.append(car) # não é necessario usar o else aqui pois não roda se der o TypeError.
        
ford = Garage()
# ford.add_car('Fiesta') # Acontece NotImplementedError
# ford.add_car2('Fiesta') # Acontece TypeError

car = Car('Ford', 'Fiesta')
ford.add_car2(car)
print(len(ford))
