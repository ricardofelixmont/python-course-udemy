#!/usr/bin/env python3
# Create Stored movies with object-oriented programming:

class Movie:
    """ 
    Classe Filmes
            Tem os atributos:
                titulo, diretor e ano de lançamento.
    """
    def __init__(self, new_title, new_director, new_year=1994):
        self.title = new_title
        self.director = new_director
        self.year = new_year

class Agencia:
    """ 
        Classe gerencia os objetos do tipo Movie.
    """
    def __init__(self, title, director, year):
        self.filme = Movie(title, director, year) # cria um objeto do tipo movie
        self.lista_filmes = list()
    
    def armazenar(self):
        self.lista_filmes.append(self.filme)

title = str(input('Type the name of the title: '))
director = str(input('Type the name of the director: '))
year = int(input('Type the year: '))
agencia = Agencia(title, director, year)

print(agencia.filme.title)
agencia.armazenar()
print('lista', agencia.lista_filmes)  # Printa a lista de objetos
print(f'Filme: {agencia.lista_filmes[0].title}') # lilsta_filmes[0] é um objeto do tipo Movie


