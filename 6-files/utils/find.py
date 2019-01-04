# Digamos que quero importar o modulo 'module.py'

# import utils.commom.module  -> chamado de caminho absoluto
# import .commom.module   -> da erro de sintaxe quando executamos 'python3 find.py' porém quando executamos como um importe de outro arquivo, ele funciona normalmente.
                        # isso acontece pois ele tenta fazer __main__.commom.module, o que não é possivel pois __main__ nao é um package.
import commom.module # -> dessa forma ele roda das duas formas, tanto como modulo, quanto como script. A forma acima e essa forma sao chamadas de caminho relativo. 
                     # Ele começa a procurar a partir do diretorio atual

from commom.module import save_to_file


class NotFoundError(Exception):
    pass  # como nao temos nenhum argumento alem da mensagem de erro

def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i

    raise NotFoundError(f'{expected} not found in provided iterable.')

print('find.py', __name__)
