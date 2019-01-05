import sqlite3

connection = sqlite3.connect('data.db')  # data é um arquivo único onde são armazenados os dados. Podemos colocar qualquer nome, porém a convensão é 'data.db'
cursor = connection.cursor()   # depois precisamos criar um cursor

cursor.execute('Your SQL Query Here')  # e atraves desse cursos podemos executar um comando SQL
connection.commit()     # então temos que dar o commit() para que o que foi executado que as alterações sejam salvas no banco.

connection = close()   # depois de conectarmos, sempre precisamos fechar a conecção. Bem similar ao que acontece com 'files'.





# O que é um cursor?
# Todas as operações no SQLite são feitas por um cursor, e não pelo objeto 'connection' sozinho.
# - A razão é simples: podemos ter uma conexão apenas, mas podemos ter vários cursores, que podem ler varios dados ao mesmo tempo e ainda escrever um dado por vez.
# A palavra cursor vem do fato de que quando procuramos algo em um banco é como se estivessemos apontando um cursos como o do mouse para a linha da tabela que estamos procurando.


# O que é commit?
# Salvar todas as alterações da query no disco.
# Quando executamos uma query, ele armazena os dados dessa query na memoria. Somente depois do commit() as alterações serão salvas.
# Nós podemos gravar muitas coisas juntas, o que é mais rápido.



# Alguns tipos de dados:
# integer = inteiros
# text = guarda strings
# blob = campo de dado binario onde podemos guardar imagens e arquivos em geral como .pdf
