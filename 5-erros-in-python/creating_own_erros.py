#!/usr/bin/env python3.6

# Para criar nossos proprios erros, precisamos herdar de alguma classe de Erro, por exemplo TypeError
# pode ser qualquer uma...
class MyError(TypeError):
    """
    Documentação da Classe
    """
    # message é um atributo da superclase e code é um atributo que criamos para a classe MyError()
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}') # Mensagem de erro da superclasse(TypeError), sempre precisamos colocar
        self.code = code


""" Aqui estamos criando um objeto do tipo MyError(), e passando os parametros que definimos na nossa
    classe acima. A palavra reservada 'raise' faz com que o objeto seja levantado.
"""
# raise MyError('Motivo do erro e explicacao.', 500) 
print(MyError.__doc__)  # __doc__ é o metodo magico que mostra a documentacao da classe.                

# Criando um objeto do tipo MyError
err = MyError('Motivo do erro e explicacao.', 500)
# Útil para desenvolvimento.
print(err.__doc__)



# CRIANDO MEU PROPRIO ERRO:

class MeuErro(Exception):
    """
    Herdar de Exception é melhor pois esta é a classe
    base para todas as exceções do python.
    """
    def __init__(self, message, meu_atributo): # messsage é um atributo herdado da superclasse 'Exception', porém não é um parametro obrigatorio
        
        # Posso escrever super().__init__(message): ou posso escrever tambem coisas mais complexas como abaixo:
        super().__init__(f'{message}:{meu_atributo}')   # Obs: sempre precisamos colocar o super().__init__()
        self.meu_atributo = meu_atributo


# Então posso 'raise' levantar meu erro:
raise MeuErro('Meu Erro', 'Explicação') 

