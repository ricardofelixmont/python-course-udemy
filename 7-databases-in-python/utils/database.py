#!/usr/bin/env python3.7
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
        
        """Cria um dicionario com os parâmetros recebidos"""

        movie = {"name":f'{name}', "autor":f'{autor}', "read":f'{read}'}
        books.append(movie)
        return 'success...'



class ListAll:
    @classmethod
    def list_all(cls):
        """
        Cria uma lista com todos os filmes em uma formatação:
            Nome: Exemplo
            Autor: Outro Exemplo
            Status: Lido/Não Lido
        """
        return [f'\nNome: {book["name"]}\nAutor: {book["autor"]}\nStatus: {book["read"]}' for book in books]
            
class BookStatus:
    @classmethod
    def book_status(cls, name, status):
        for book in books:
            if book["name"] == name:
                if status == 'r':
                    book["read"] = True
                    return 'marked like read...'
                elif status == 'n':
                    book["read"] = False
                    return 'marked like non-read...'
            else:
                return 'Book was not Found...'

class DeleteBook:
    @classmethod
    def delete_book(cls, name):
        for index, book in enumerate(books):
            if book["name"] == name:
                del books[index] 
        return f'The book {name} was deleted successfully...'



if __name__=='__main__':
    
    # Testing add method...
    Add.add('Senhor dos Aneis', 'Tolkien', True)
    Add.add('Silmarilion', 'Tolkien', True)
    Add.add('As duas Torres', 'Tolkien')
    Add.add('Retorno do Rei', 'Tolkien', True)
    print(books)
    
    # Testing list all books...
    print(ListAll.list_all()[0])
    print(ListAll.list_all()[1]) 

    # Testing book_status
    print(BookStatus.book_status('Senhor dos Aneis', 'r'))
    
    # testing delete_book
    DeleteBook.delete_book('Senhor dos Aneis')
