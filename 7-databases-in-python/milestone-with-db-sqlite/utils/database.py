#!/usr/bin/env python3.7

import sqlite3


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

books  = list()

class Add:
    """
    Add a movie to our database(for while it's a list) called 'books'
        parameter1: 'name' its the movie name.
        parameter2: 'autor' its the movie autor name.
        parameter3: 'read' it marks the book whether its read(True) or not(False)
    return: It doesn't have return. It just append the movie to the list.
    """
    @classmethod
    def add(cls, name, autor, read=0):  # instead of False as default we put zero, because the datatype in db is 'integer'
        
        """Adiciona um novo livro ao banco de dados SQLite"""
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        

        # Não é seguro fazer as querys usando f strings pois isso permite que o usurario coloque seuas proprias querys como
        # Sendo o nome dos usurários e seu autos. Isto é chamado de SQL Injection Attack
        # cursor.execute(f'INSERT INTO books VALUES("{name}", "{autor}", "{read}")')
        # A melhor maneira de fazer isso é:
        cursor.execute('INSERT INTO books VALUES(?, ?, ?)', (name, autor, read))
        connection.commit()
        connection.close()
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
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        livros = cursor.fetchall()
        books = [{'name': row[0], 'autor':row[1], 'read': row[2]} for row in cursor.fetchall()]   # cursor.fetchall() retorna um lista de tuplas.
        connection.close()
        return livros


class BookStatus:
    @classmethod
    def book_status(cls, name, status):
        if status == 'r':
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))
            connection.commit()
            connection.close()
            return 'marked like read...'

        elif status == 'n':
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            cursor.execute('UPDATE books SET read=0 WHERE name=?', (name,))
            connection.commit()
            connection.close()
            return 'marked like non-read...'
        else:
            return 'Book was not Found...'


class DeleteBook:
    @classmethod
    def delete_book(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        cursor.execute('DELETE FROM books WHERE name=?', (name,))
        connection.commit()
        connection.close()
        return f'The book {name} was deleted successfully...'


class CreateBookTable:
    @staticmethod
    def create_book_table():
        """
        1. Cria o banco e se conecta a ele.
        2. Cria a tabela 'books' onde serão armazenados os dados dos livros
        """
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, autor text, read integer)')
        connection.commit()
        connection.close()


if __name__=='__main__':

    novo = 'Novo2'
    print(DeleteBook.delete_book(novo))
    print(ListAll.list_all())
