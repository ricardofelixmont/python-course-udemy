#!/usr/bin/env python3

import string

# Significado do self
class Person(object):
    # método
    def set_sobre_nome(person, sobre_nome):
        person.sobre_nome = sobre_nome

# As funções relacionadas aos objetos dentro do método 
# é uma convenção de POO pois torna o codigo mais legivel e 
# define melhor as 'responsabilidades' de cada classe
def set_name(person, name):
    # Não aceita nomes com menos de duas letras
    if len(name) >= 2:
        person.name = name

woman = Person()
# Usando a função set_nome que está fora da função, no objeto woman
set_name(woman, 'Juliana')

# Invocando o método 'set_idade' no objeto woman.
woman.set_sobre_nome('Julia') 
print(woman.name)
print(woman.sobre_nome)

# Herdando:
class CapitalizedPerson(Person): # inheritance of Person
    def set_name(self, sobre_nome):
        if sobre_nome[0] in 'R':
            # para utilizar o método set_sobre_nome da classe Person, 
            # precisamos colocar 'Nome_da_classe.metodo(argumento)'
            Person.set_sobre_nome(self, sobre_nome)

man = CapitalizedPerson()
man.set_name('Ricardo')
print(man.sobre_nome)


# EXERCICIO Herança:
class Pessoa:  # SuperClasse
    def __init__(self, name, age): # Contrutor recebe dois atributos, 'name' e 'age'
        self.name = name
        self.age = age
    @property
    def overage(self): # Passo o objeto self, pois posso usar qualquer atributo dele como por exemplo 'age' com 'self.age'
        '''Mesmo tendo duas possibilidades de retorno,
        ele só retorna um de cada vez, então posso usar 
        o @property para usar uma função como se f
        osse um atributo'''
        if self.age >= 18:
            return 'Overage' 
        else:
            return 'UnderAge'

class Aluno(Pessoa): # aluno herda de pessoa
    def __init__(self, name, age, grades): # Construtor da classe filha, tem que ter todos os paramentros dela e da SuperClasse
        self.grades = grades
        super().__init__(name, age)
        

    def average(self): # Passo o objeto como argumento, Poderia ser uma lista, que não faz parte da classe
        return sum(self.grades) / len(self.grades)

aluno = Aluno('Lucas', 18, [50, 80, 70, 60])
print(f'{aluno.name}, {aluno.age}, {aluno.grades}')
print(f'Média: {aluno.overage}')


