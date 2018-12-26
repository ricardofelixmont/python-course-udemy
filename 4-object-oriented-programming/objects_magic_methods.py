#!/usr/bin/env python3.6
# TUDO EM PYTHON É UM OBJETO

# MÉTODOS MÁGICOS

movies = ['Matrix', 'Finding Nemo']
print(len(movies))
print(movies.__class__)
print('hi'.__class__)



# Garagem
class Garage:
    def __init__(self):
        self.cars = []
    
    def __len__(self):
        """ 
        Este método magico habilita o uso 
        do da função len() neste objeto.
        """
        return len(self.cars)

    def __getitem__(self, index):
        """
        Este método mágico habilita o uso 
        da indexação ao objeto Garage.
        Também nos habilita a usar o 'for loop' para 
        iterar sobre os itens desse objeto
        """
        return self.cars[index]

    def __repr__(self):
        # O professor recomenda utilizar esses dois métodos sempre que 
        # criamos uma classe
        """
        É preferivel usar __repr__ do que o __str__, pois o __repr__ 
        é utilizado quando estamos programando, muito util em debbuging
        Este método é usado para printar uma 
        string com a descrição do objeto do tipo Garage.
        """
        return f'<Garage {self.cars}>'
    
    def __str__(self):
        """
        É o que aparece para o usuário quando usamos a função print().
        Serve para dar ao usuario algumas informações sobre o objeto
        do tipo Garage. Algo mais util para o usuario do que apenas 
        o que é retornado no metodo __repr__
        """
        return f'Garage with {len(self)} cars'

ford = Garage()  # Instanciando o objeto 'ford' do tipo 'Garage'
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(ford.cars)
print(len(ford.cars)) # with out the magic method __len__ we can't use the 
                      # method len() to receive the lenght of the list or object
print(len(ford))
print(ford[0]) # preciso do metodo magico 
print(ford.__getitem__(0))  # é o mesmo que na lista acima

c = 0
# Podemos iterar sobre o objeto for, gracas ao metodo magigo 
# __getitem__
for car in ford:
    print(c,'-',car)
    c += 1

print(ford)
