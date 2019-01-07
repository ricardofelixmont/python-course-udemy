# Como criar context manager:
"""
class MyContextManager:
    def __init__(self):  # Opcional, utilizamos apenas quando queremos inicalizar alguama variavel
        pass
    
    def __enter__(self):
        
        self.variavel = 'o que ela tem que receber'  
        return self.variavel     # ela vai retornar 'with MyContextManager() as 'self.variavel':

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.variavel = variavel * 2


Ou seja:

class MyContextManager:
    def __init__(self):
        # Inicializa as variaveis que vem como parametro
        pass

    def __enter__(self):
        # Faz a ação inicial
        pass
    def __exit__(self):
        # Faz a ação final, depois que ja usamos a informação.
"""

import sqlite3

class DatabaseConnection:
    def __init__(self, host):
        self.connection = None
        self.host = host

    def __enter__(self):   # Aqui fica tudo que acontece quando abrimos o arquivo
        self.connection = sqlite3.connect(self.host)
        return self.connection   # Faz o connection = sqlite3.connect("data.db")

    # Só funciona se tiver todos os parametros como abaixo:
    def __exit__(self, exc_type, exc_val, exc_tb):    # Tudo que acontece depois que usamos o arquivo
        # Se algum erro acontecer durante o __enter__, mesmo assim o programa vem para o __exit__ e passa o erro como argumento para
        # o exc_tb e um dos outros dois parametros acima.
        # Para que o programa nao feche podemos fazer o seguinte:

        if exc_type or exc_val or exc_tb:    # é o mesmo que 'if exc_type is not None or exc_val is not None or exc_tb is not None:'
            self.connection.close() # se algum erro ocorrer la em cima, a connecção é fechada e nada acontece.
        else:
            self.connection.commit()  # Mesmo se eu usar quando tem um select, ele nao vai dar erro... entao posso deixar esse commit() aqui normalmente.
            self.connection.close()
        

"""
    Entendendo melhor os argumentos de __exit__

    exc_type = tipo de exceção que foi levantada, por exemplo NotImplementedError
    exc_val = valor da exceção, para exceções que retornam algum valor, alguma mensagem...
    exc_tb = traceback exception, armazena o traceback exception da exceção.
"""
