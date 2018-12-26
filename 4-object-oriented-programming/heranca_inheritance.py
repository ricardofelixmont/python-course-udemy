#!/usr/bin/env python3
# Vamos agora trabalhar com herança em PPO Python 

# Digamos que temos a classe Student abaixo:
class Student:
    def __init__(self, name, school):
        print('Construtor da super Clase')
        self.name = name
        self.school = school
        self.marks = list()

    def average(self):
        return sum(self.marks) / len(self.marks)


# Caso eu quisesse adicionar funcionalidades a essa classe 
# poderia criar outra:
class WorkingStudent:
    def __init__(self, name, school, salary):
        self.name = name
        self.school = school
        self.marks = list()
        self.salary = salary
# Não é uma boa pratica fazer isso, pois estamos duplicando código

rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.salary)

# IMPLEMENTANDO A CALSSE WorlingStudent novamente:
class WorkingStudent2(Student): # WorkingStudent herda de Student
    def __init__(self, name, school, salary):
        print('construtor da Subclasse')
        super().__init__(school, name)  # chama o construtor da superclasse
        self.salary = salary
    
    # Posso adicionar também metodos na subclasse
    def weekly_salary(self):
        return float(self.salary) * 37.5
    """
    TypeError: can't multiply sequence by non-int of type 'float'

    Se eu não der casting para float acontece o erro descrito no link abaixo:
    https://pt.stackoverflow.com/questions/176627/cant-multiply-sequence-by-non-int-of-type-float
    """
new_student = WorkingStudent2('Vitor', 'São Judas', '1200')
print(new_student.salary)
new_student.marks.append(57)
new_student.marks.append(99)
print(new_student.average())
print(new_student.weekly_salary())

