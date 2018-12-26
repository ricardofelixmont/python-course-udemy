#!/usr/bin/env python3
my_student = {
        'name':'Natalia',
        'grades':[70, 88, 90, 99] # aqui o ideal seria colocar uma função
                                  # que calcula a media, porem um dicionario 
                                  # não nos permiter fazer isso.
        }
# Função que calcula a média de my_student
def average(student):
    average = sum(my_student['grades'])/len(my_student['grades'])
    return average

print(average(my_student))

# Essa não é a melhor maneira de fazer isso
# Podemos criar um objeto para fazer isso, armazenar dados e funções

class Student:
    # __init__ = dunder function "Double Underscore" , they're called special or    # magic methods

    # __init__ é o construtor em python, é o metodo chamado quando instaciamos
    # uma classe
    def __init__(self, new_name, new_grades): # quando é instanciado
                                             # 'self' é um objeto vazio em branco
        # 'self' pode ter qualquer nome
        # POREM É CONVENSÃO USAR O NOME DO PRIMEIRO PARAMENTRO DE UMA CLASSE COMO 'self'
        # exemplo: def __init__(new_object, new_name, new_grade):

        self.name = new_name # Criando uma variavel com o atributo name
        self.grades = new_grades # O mesmo aconteceu com grades
        # depois dessa linha o objeto self ja não é mais vazio

    def average(self):
        return sum(self.grades)/len(self.grades)

# Quando criamos o objeto, o 'self' 
student_one = Student('Shrek', [70, 88, 90, 99]) # Creating my first object in python
print(f'Nome: {student_one.name}\nNotas: {student_one.grades}\nMédia: {student_one.average()}')
print(student_one.__class__) # mostra o tipo do objeto, no caso student_one


""" 
    Quando invocamos o metodo average(self), o argumento self é 
    preenchido automaticamente com o objeto a qual a funcao foi referenciada,
    nesse caso, o objeto 'student_one'
"""
print('Mostra média: ', student_one.average())
# podemos fazer tambem atraves da classe:
print('Mostra média: ', Student.average(student_one)) # porém precisamos colocar o objeto que queremos que tome o lugar de self como argumento


# Podemos criar tambem funções fora da classe para calcular a media, ou manipular os atributos:
def average(student):  # passamos uma instancia da classe 'Student' como argumento para a função
    return sum(student.grades)/len(student.grades)   # dessa forma podemos chamar os atributos desse obejto

print('Usando função fora da classe para calcular a media: ', average(student_one))



# UTILIZANDO MAIS DE UM PARAMETRO NO METODO
class Professor:
    def __init__(self, nome, materia, salario):
        self.nome = nome            # self.atributo = parametro -> esse atributo vira uma variavel quando instanciamos um objeto
        self.materia = materia
        self.salario = salario
     
    def show_professor(self, message):
        print(message, self.nome)

new_professor = Professor('Carlos', 'Fisica', '1300')
new_professor.show_professor('Olá ')


# Exercicio, crie uma classe movie com atributos titulo e diretor
# e instacie um objeto

class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director
    
    def print_info(self):
        print(f'{self.title} by {self.director}')

movie_object = Movie('Matrix', 'desconhecido')
print(f'Title: {movie_object.title}\nDirector: {movie_object.director}')
movie_object.print_info()
