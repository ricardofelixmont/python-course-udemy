from utils.commom.module import read_file  # coloco o nome do diretorio e depois o nome do módulo, quando estou usado esses modulos em diretorios diferentes.
                                           # o caminho sempre parte do diretorio onde 'este modulo' esta.
                                           # O NOME DA PASTA/DIRETORIO ONDE OS ARQUIVOS QUE SERAO IMPORTADOS ESTÃO É: 'package'
                                    

                                    # em versões anteriores do python era necessario criar um arquivo chamado '__init__.py' vazio detro do package para que ele fosse identificado como package e
                                    # só entao poder importar modulos dele. Packages sao diretorios onde guardamos modulos do python estão.

print(read_file('data.txt'))

print(__name__) # name guarda o nome do módulo, que é sempre '__main__'



# CHILDREN 
# commom é uma child de util, funciona da mesma maneira que o css selctor
# PARENTS
# util é parent de commom, utilizando a notação de ..commom.module da na mesma que utils.commom.module.

# OBS: QUANDO UTILIZAMOS CAMINHOS RELATIVOS PARA IMPORTAR UM ARQUIVO, ELE NÃO PODERÁ SER EXECUTADO COMO UM SCRIPT A PARTE, SOMENTE DENTRO DE OUTRO
# MODULO.
