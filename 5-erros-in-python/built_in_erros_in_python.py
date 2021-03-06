"""
    VAMOS VER OS SEGUINTES ERROS:
    1. IndexError
    2. KeyError
    3. NameError
    4. AttributeError
    5. NotImplementedError
    6. RuntimeError
    7. SyntaxError
    8. IndentationError
    9. TabError
    10. TypeError
    11. ValueError
    12. ImportError
    13. DeprecationWarning


1. IndexError
    Acontece quando tentamos acessar um index que não existe ou 
    um index que é incorreto.

2. KeyError
    Acontece quando usamos uma key(em dicionarios) de maneira incorreta, 
    ou a key não existe.

3. NameError
    Acontece quando a variavel não foi definida.

4. AttributeError
    Acontece em orientação a objeto. Quando tentamos invocar um método
    que não existe naquela classe.

5. NotImplementedError
    Não é um erro que acontece com muita frequencia, mas é um erro que 
    na verdade podemos usar.
    Se chamarmos a função login(), acontecerá o NotImplementedError.
"""
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        # Esta é a maneira como podemos 'levantar' erros em python.
        # Achei parecido com o que acontece com as interfaces e métodos 
        # abstratos em java.
        raise NotImplementedError('Esta função ainda não foi implementada.')
        
"""
6. RuntimeError
    É um erro generico, é essencialmente um erro base, uma classe base
    e outros erros herdam dela. 
    Basicamente é um erro que acontece enquanto rodamos um programa.

7. SyntaxError
    Acontece quando erramos a sintaxe do python. 
    por exemplo:
    
    class User
        def function(self):
            pass

    No codigo acima nós esquecemos o ':' na frente do nome da classe.

8. IndentationError
    Exemplo:
    
    def funcao(x):
    return x * 2
    
    O rerturn acima não está indentado da maneira correta.

9.  TabError
    É um erro que acontece muito quando trocamos de editor de texto.
    Ao usarmos quatro espaços para indentar e usar tab também no mesmo documento
    podemos nos deparar com esse erro. Por isso é importante escolher um 
    padrão para adotar, ou espaços ou tabs. Não é bom misturar.

10. TypeError
    É um erro muito comum em python. 
    exemplo: 

    5 + 'hi' -> no codigo ao lado estamos tentando somar um int e uma string
    Isso levantar o "TypeError"

11. ValueError
    Também é um erro muito comum. 
    Normalmente, só built-in functions vão levantar ValueError
   
    É importante ressaltar que se quisermos dar 'raise' em ValueErrors é melhor nossos próprios erros.

12. ImportError
    Um exemplo: onde fazemos imports de maneira circular, dando voltas em circulo, importar um arquivo
    que importa o mesmo arquivo.

    # arquivo app.py
    import blog

    def menu():
        pass

    # arquivo blog.py
    from app import menu

    def do_something():
        pass

        
13. DeprecationWarning
    É um warning, não um erro. Deprecated significa que esta não é a melhor maneira de fazer aquilo.
    Apesar de ser um warning ele é tratado da mesma maneira que um erro no python.

Exemplo:
"""

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        print(self.password, self.username)
        raise DeprecationWarning('User#Register still works, but is deprecated')

    @classmethod
    def register_user(cls, username, password):
        print(self.password, self.username)
        return cls(username, password)

novo = User('Ricardo', '123')
novo.register()

# Se rodarmos o programa vai acontecer o seguinte warning:
'''Traceback (most recent call last):
  File "built_in_erros_in_python.py", line 131, in <module>
    novo.register()
  File "built_in_erros_in_python.py", line 123, in register
    raise DeprecationWarning('User#Register still works, but is deprecated')
DeprecationWarning: User#Register still works, but is deprecated'''


# CONSIDERAÇÕES E OBSERVAÇÕES:
# Possivelmente não vamos dar 'raise' em nenhuma dessas exceções.
# Devemos criar nossas proprias exceções com nomes e descrições apropriadas para cada caso.

