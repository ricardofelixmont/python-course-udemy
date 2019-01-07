# Vamos adicionar mais funcionalidades ao projeto da seção 7.

""" Com type hinting, podemos fazer com que fiquem mais claros o que cada função faz, 
    que valores elas estão esperando e quais seus retornors.
    É uma ótima técnica para adicionar nos nosso programas.
     Type hinting é um conceito mais avançado em python.
"""

""" python é conhecida como uma linguagem dinâmica: em uma linguagem dinâmica nós não especificamos o tipo de dados que uma 
    variável tem."""


'''Por exemplo, em java temos:
    Cursor cursor = connection.cursor()
    
    temos que especificar qual o tipo de variavel nós queremos
    
    int x = 10
    float y = 20
   
    Isso acontece por que o java é uma "statically typed language" onde precisamos especificar os tipos de dados quando criamos uma variavel.
    O python como é uma linguagem dinâmica, não precisamos fazer isso.
    
    -> A vantagem de se ter uma linguagem dinâmica é que precisamos escrever menos codigos por não precisamos ficar especificando tipos o tempo todo.
    -> A desvantagem é que as vezes quando vamos utilizar uma variavel em programas maiores, podemos não saber o tipo exato dela. Isso pode não ficar        muito claro.
    Exemplo:
        declaramos uma tupla no começo de um programa:
        friends = ('Jose', 'Amigo2')
        
        vamos dizer que mais pra frente no programa queremos fazer o seguinte:
        friends.append('Novo Amigo'), obviamente isto não dará certo, e nesse caso fica facil de saber o que aconteceu. Porém em programas maiores, 
        com muitas pessoas colaborando, pode ser muito mais dificil identificar esses problemas. 


    Por esses motivos a partir do python3 foi adicionada uma funcionalidade, o type hinting.

'''


def mensagem(message) -> None:  # -> serve para que saibamos que quando utilizamos essa função, esperamos receber None como retorno.
                                 # -> isto é um type hint
    print(message) 


# quando fizermos: 
my_variable = mensagem('Minha mensagem como argumento')

""" 
    No caso acima, o pycharm ou outras IDEs vão sinalizar que my_variable não retorna nada,
    pois adicionamos o type hinting '-> None'. Ele vai sinalizar siginifica mais ou menos isso: 
        'Essa função retorna None, tem certeza que quer atribui-la a uma variavel?"
    
    Vale ressaltar que os type hintings só são uteis quando estamos desenvolvendo em IDEs como Pycharm entre outros.
"""

# Mesmo fazendo:
mensagem('Minha mensagem como argumento')
# podemos deixar -> na função pois o python não força o uso obrigatorio dos type hintings.


# Outro exemplo:
# Para usar o List[Dict] precisamos importar o módulo de type hinting:

from typing import List, Dict, Union

def nomes(dicionario) -> List[Dict]:  # A IDE vai sinalizar que esperamos receber uma lista de dicionarios como retorno dessa função.
    lista = list()
    lista.append(dicionario)

    return lista

dict_list = nomes({"Nome": "Meu Nome"})
print(dict_list)


# PODEMOS AINDA ESPECIFICAR OS TIPOS DE DADOS QUE O DICIONARIO PODE RECEBER COMO CHAVE E VALOR:
def nomes2(dicionarios) -> List[Dict[str, Union[str, str]]]:
    lista = list()
    lista.append(dicionarios)

    return lista


# Podemos ainda definir o tipo de variavel que será recebido como parâmentro.
def nomes3(nome: str, sexo: str) -> None:        # O pycharm vai sinalizar caso façamos: nomes3(5, 'feminino') pois '5' é um
                                                 # inteiro e ele espera receber uma string
    print(f'{Nome} {sexo}')


def nome(nome: str, sexo: str) -> List[Dict]:
    print(f'{nome} {sexo}')
    lista = []
    lista.append({"nome":nome, "sexo":sexo})
    return lista

nome('Ricardo', 'Masculino')


from typing import List, Dict, Union

def nome(nome: str, sexo: str) -> List[Dict[str, Union[str, Union[int, str]]]]:  # Sempre preciso usar colchetes [] para que funcione no'vim' tambem
    print(f'{nome} {sexo}')
    lista = []
    lista.append({"nome":nome, "sexo":sexo})
    return lista

nome('Ricardo', 'Masculino')



# Posso definir os tipos antes para que fique mais legivel: 
Book = Dict[str, Union[str, int]]

def books(livro) -> List[Book]:
    lista = []
    lista.append(livro)
    return lista

livros = books({"livro":"Senhor dos Aneis"})
print(livros)


""" É realmente recomendado fazer uso de Type Hints para melhorar a legibilidade dos códigos e
    também ajudar a evitar problemas como os citados acima a medida que o projeto fica maior."""

