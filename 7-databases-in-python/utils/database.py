"""
Concerned with storing and retrieving books from a list.
"""


""" Estrutura dos livros:
    Cada livro será um dicionario:

    {
    "name":'Peter Pan',
    "autor":'Desconhecido",
    "read":False  # or True
    }
"""

books = list()


class Add:
    """
    Add a movie to our database(for while it's a list) called 'books'
        parameter1: 'name' its the movie name.
        parameter2: 'autor' its the movie autor name.
        parameter3: 'read' it marks the book whether its read(True) or not(False)
    return: It doesn't have return. It just append the movie to the list.
    """
    @classmethod
    def add(cls, name, autor, read=False):

        movie = {"name":f'{name}', "autor":f'{autor}', "read":f'{read}'}
        books.append(movie)
        return 'success...'


if __name__=='__main__':

    # Testing add method...
    Add.add('Ricardo', 'Mãe')
    print(books)
    
