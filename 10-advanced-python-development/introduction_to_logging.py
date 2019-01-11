# O logg é essencialmente tudo que aconteceu na sua aplicação durante o tempo de execução.
""" Onde podemos usar logs?
            * para mostrar problemas que aconteceram quando o programa foi executado e podermos analisar e concertar.

        Em programas pequenos não é útil, porém em grandes projetos os loggs são essencialmente necessários.
        O interessante do modulo logging do python é que podemos organiza-lo em varios niveis. Podendo desativar o que nao precisamos.
    """

# O módulo de logging é basicamente usado para printar coisas.


import logging
logging.basicConfig(level=logging.DEBUG)

# Depois de importar o modulo logging, a primeira coisa que precisamos fazer é criar uma variavel 'logger':
logger = logging.getLogger('test_logger')

# Para printar coisas podemos usar por exemplo:
logger.info('This will not be shown.')
logger.warning('This message will be shown.')


"""
    Niveis de logging

DEBUG (usar apenas quando estamos deselvovendo)
INFO
WARNING
ERROR
CRITICAL
"""
