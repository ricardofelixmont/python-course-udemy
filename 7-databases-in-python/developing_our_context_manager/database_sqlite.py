import sqlite3
from context_manager_connection import DatabaseConnection


# SEMPRE TEMOS QUE INICAR COM ESSAS DUAS LINHAS:
connection = sqlite3.connect('data.db')
cursor = connection.cursor()


# cursor.execute('INSERT INTO books VALUES("Ricardo", 25)')
# cursor.execute('INSERT INTO books VALUES("Érika", 24)')
cursor.execute('SELECT * FROM books')
lista = dict(cursor.fetchall())


# Sempre acontece quando terminamos de fazer a QUERY:
connection.commit()
connection.close()




# UTILIZANDO MEU PROPRIO CONTEXT MANAGER
nomes = list()
with DatabaseConnection('data.db') as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    nomes = cursor.fetchall()

print(dict(nomes))

