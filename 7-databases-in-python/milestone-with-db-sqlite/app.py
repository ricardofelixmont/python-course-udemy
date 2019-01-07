#!/usr/bin/env python3.7
from utils import database
from os import system


USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    database.CreateBookTable.create_book_table()
    user_input = ''
    while user_input != 'q':
        user_input = input(USER_CHOICE).lower()
        if user_input == 'a':
            name = input('Name: ')
            autor = input('Autor: ')
            
            system('clear')
            print(database.Add.add(name, autor))

        elif user_input == 'l':
            x = database.ListAll.list_all()
            system('clear')
            print('Lista de Filmes'.center(21, '='))
            print(x)
            print('\n')
            print('Fim'.center(21, '='))

        elif user_input.lower() == 'r':
            book_name = input('Type the book name: ')
            status = input('\nHow do you want to mark this Book?\nRead[r]\nNon-Read[n]\nQuit[q]: ')
            if status == 'q':
                continue
            while status not in 'rn':
                status = input('\nHow do you want to mark this Book?\nRead[r]\nNon-Read[n]\nQuit[q]: ')
            if status in 'rn':
                system('clear')
                print(database.BookStatus.book_status(book_name, status))
        elif user_input.lower() == 'd':
            book_name = input('Type the book name: ')
            confirmation = input('Do you realy want to delete {book_name} [S/N]? ').lower()
            while confirmation not in 'sn':
                confirmation = input('Do you realy want to delete {book_name} [S/N]? ').lower()
            if confirmation == 's':
                system('clear')
                database.DeleteBook.delete_book(book_name)
            else:
                print('Invalid option, try again...')
                continue
    print('The program was quit...')



if __name__=='__main__':

    menu()

