#!/usr/bin/env python3.6
# lets imagine we hava a car park:

class LenMixin:
    """ Documentação da Classe LenMixin""" # Essa documentação não aparece
    def __len__(self):
        return len(self.carros)
    def __repr__(self):
        return f'Object description'

class Estacionamento(LenMixin):
    """
    Documentação da Classe.
        Herdando de LenMixin.
    É importante ressaltar que a documentação da Classe fica aqui.
    """
    def __init__(self, carros): # Objeto vazio self, e um parametro carros
        self.carros = carros

estacionamento = Estacionamento(['Corolla', 'Etios', 'Hilux', 'Sandero', 'Fluense', 'Clio'])
print(estacionamento.carros)

# Vamos supor que queremos utilizar o metodo len() para saber quantos carros temos dentro do estacionamento naquele momento
# Podemos implementar o método magico dentro da classe Estacionamento(), porém se tivermos mais classes que precisem desse metodo
# teriamos que implementar um por classe, o que é duplicar código. Ao invez disso podemos criar um classe a parte:

# Então criamos um objeto Estacionamento que herda de LenMixin
estacionamento2 = Estacionamento(['Corolla', 'Fiesta', 'Focus'])
print(estacionamento2.carros)
print(len(estacionamento2))
print(estacionamento)
print(estacionamento.__doc__) # Mostra a documentação da classe
