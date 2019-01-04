# O módulo file_operations ja foi importado no modulo find. Então o python reconhece que existe o mesmo modulo sendo importado duas vezes.
# pois ele cria um dicionario global de módulos importados.
# Analisando os dois casos:
# from file_operations import add  # da import error 
import file_operations # não da import error.


def find_in(number):
    for c in range(0,number):
        if c == number:
            return n

    raise NotFoundError(f'{expected} not found in provided iterable.')


class NotFoundError(Exception):
    pass

print(__name__)

# se quisermos testar as funções desse módulo, porém queremos que esses testes não apareceçam quando este for importado por outro módulo:
if __name__=='__main__':
    print('Testando o módulo')

