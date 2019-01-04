#!/usr/bin/env python3.7
from utils import database


USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


user_imput = ''
def menu():
    user_input = input(USER_CHOICE)
    while user_imput != 'q':
        if user_imput == 'a':
            name = input('Name: ')
            autor = input('Autor: ')
            
            print(database.Add.add(name, autor))
            break

menu()
