from time import sleep

"""
      Função de exemplo com algumas anotações.
      Argumentos:
          data: é uma lista de dicionarios.
          index: não serve para nada pois estou usando dicionario, só mantive pois o assert me obrigou.
      Retorna:
          Uma lista de elementos de uma coluna.
"""


# Studying Object-Oriented in python

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

 
class Aluno(Person): # Herda de Person
    def __init__(self, name, age, gender, grades):
        super().__init__(name, age, gender)
        self.grades = grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)

lista_alunos = list()
nome = str(input('Type a name: '))
idade = int(input('Type an age: '))
sexo = str(input('Type the gender: '))
notas = str(input('Type the grades with ",":')).split(',')

aluno = Aluno(nome, idade, sexo, notas)
lista_alunos.append(aluno)
print(lista_alunos[0].grades)
