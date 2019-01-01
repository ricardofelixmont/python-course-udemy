#!/usr/bin/env python3
# ENTENDENDO HERANÇA
'''
   Herança múltipla é herança: Antes de falarmos de herança múltipla,
   vale lembrar que herança múltipla é herança. Portanto, alguns comportamentos    básicos e previsíveis de herança funcionam da mesma forma.
'''

class Mae:
    def mm(self):
        print("Mãe")

    def ff(self):
        print('Classe Mãe')


class Filha(Mae):
    '''ao invocarmos um método existente na classe base e que foi
       redefinido na classe derivada, o da classe derivada é que será executado
    '''
    def ff(self): 
        print('Classe Filha')


# A classe derivada herda métodos e atributos que foram definidos na classe base
f = Filha()
f.mm()

# A classe derivada pode modificar métodos e atributos 
# que foram definidos na classe base
f.ff()
print('-=' * 30, '\n')


# Entendendo Herança Multipla:
'''
Todo mundo conhece o Pato Donald e sua namorada, a Margarida. Donald tem 3 sobrinhos, Huguinho, Zezinho e Luizinho. Margarida, por sua vez, tem 3 sobrinhas, Lalá, Lelé e Lili.

As crianças precisam obedecer tanto ao Donald, quanto à Margarida, mas os meninos dão prioridade ao que o tio diz. Enquanto que as meninas dão mais atenção ao que a tia fala.

Com esse pano de fundo, vamos iniciar nossa explicação sobre herança múltipla em Python.
'''

# OS ADULTOS: Os adultos são a base das famílias. Aqui, cada um deles é representado por uma classe:

class Margarida:
    # construtor
    def __init__(self): # Não recebo parametros para criar 'Margarida'
        print('init da Margarida')
        self.responsavel = 'Tia Margarida'

    def criancas(self):
        print('Lalá, Lelé, Lili')

class Donald:
    def __init__(self):
        print('init do Donald')
        self.responsavel = 'Tio Donald' 

    def criancas(self):
        print('Huguinho, Zezinho e Luizinho')

    def amigos(self):
        print('Mickey e Pateta')

# Testando as classes:
print('TESTANDO AS CLASSES:')
donald = Donald()
print(donald.responsavel)
margarida = Margarida()
print(margarida.responsavel)
print('-=' * 30)
print('\n')


# TESTANDO HERANÇA MULTIPLA
'''A seguir, criaremos uma classe derivada para analisarmos alguns cenários:

        Instanciar um objeto da classe derivada;

        Invocar método da classe base usando super();

        Invocar métodos das classes base explicitamente;

        Sobrepor um método da classe base.
'''

'''As crianças
Nosso primeiro exemplo de herança múltipla.

Vou criar a primeira versão da classe derivada bem simples.
Ela será vazia, ou seja, não vai acrescentar nada às classes base,
mas vai herdar de duas classes:
'''
'''# Herda de margarida e de Donald ao mesmo tempo:
class Sobrinha(Margarida, Donald):
    pass
print('Observando o comportamento de heranças multiplas')
# Vamos ver o que acontece ao instanciar a classe derivada:
lala = Sobrinha()
lala.criancas()
print(lala.responsavel)'''

'''Analisando o que fizemos e o resultado:

1. Criamos a classe Sobrinha que implementa herança múltipla, herdando de Margarida e de Donald;

2. A classe Sobrinha não tem nenhum método nem atributo adicional aos que já existem em Margarida e em Donald;

3. Criamos uma instância da classe Sobrinha, chamada lala;

4. O método Margarida.__init__() foi executado;

5. lala.responsavel mantém o conteúdo atribuído em Margarida.__init__().

Podemos concluir uma coisa desse comportamento básico: nenhum método da classe Donald foi invocado. Ou seja, é a Margarida quem manda em uma Sobrinha.

Quem está iniciando em Python poderia perguntar:

Por que Margarida.__init__() foi executado, se o objeto lala não manda fazer isso?

A resposta é simples: porque __init__() é executado sempre que um objeto é instanciado. É como se ele fosse o construtor da classe. E, como vimos anteriormente, quando um método é invocado e ele não existe na classe derivada, o da classe base é executado.

Agora, vamos criar uma nova classe derivada, ligeiramente diferente da que já temos:
'''

# Herda de Donald e de Margarida ao mesmo tempo
'''class Sobrinho(Donald, Margarida):
    pass'''

'''O que essa nova classe Sobrinho tem de diferente em relação à Sobrinha? Quase nada, apenas a ordem das classes base.

Qual será o efeito dessa inversão das classes base?'''
'''huguinho = Sobrinho()
print(huguinho.responsavel)
'''
'''Notou? Mudou tudo. Agora os métodos da classe Donald foram executados e nada de Margarida.

Com isso, aprendemos a primeira lição: a sequência das classes base faz toda a diferença na classe derivada.

Quando uma classe derivada precisa executar um método que não existe nela, o Python procura nas classes base, da direita para a esquerda, e executa apenas o primeiro que encontrar.

Por isso, quando instanciamos o objeto lala, Margarida.__init__() foi executado e com o objeto huguinho, foi a vez de Donald.__init__().

Esse comportamento simples é a base para todo o funcionamento de herança múltipla. Entendido esse ponto, tudo fica claro.'''


# FAZER O QUE O RESPONSAVEL MANDA
'''Usando as mesmas classes dos exemplos, vamos adicionar um método novo na classe derivada, para invocar métodos das classes base com super():
class Sobrinha(Margarida, Donald):
    def todos(self):
        # print (super().responsavel) # Não funciona
        super().criancas()
        super().amigos()

lala = Sobrinha()
lala.todos()'''

'''Percebeu um detalhe? Só as meninas foram listada como crianças. Por que? Porque as duas classes base definiram o método criancas() e Margarida tem prioridade para a Sobrinha.

Mas como apenas Donald tem o método amigos(), esse foi executado.

Em outras palavras, se a tia manda, a sobrinha obedece e nem ouve o que o tio diz. 
Mas quando a tia não define o que fazer, vale o que o tio disser.'''

# OUVIR AMBOS OS RESPONSÁVEIS
'''Pode ser que queiramos executar os métodos das classes base explicitamente. Um exemplo bem típico é o __init__(). Vejamos:'''

'''class Sobrinha(Margarida, Donald):
    def __init__(self):
        print('Começou')
        Donald.__init__(self)
        Margarida.__init__(self)
        print('Acabou')
'''
# Note que dessa vez invocamos explicitamente Donald.__init__() e Margarida.__init__() ao invés de usarmos 
# super().__init__(). Fizemos isso porque queremos que o __init__() de Margarida e de Donald sejam executados, 
# não apenas um deles. Além disso, queremos especificar a ordem que eles são executados.
# Vejamos o resultado:

# lala = Sobrinha()
# Os métodos __init__() da classe derivada e das duas classes base foram executados, conforme desejávamos.
# print(lala.responsavel)

'''Notou o conteúdo de lala.responsavel? Esse é um comportamento óbvio, que muitas vezes passa despercebido: quando os métodos das classes base modificam o mesmo atributo, a ação do último método executado é que fica valendo. Óbvio, mas importantíssimo. No nosso exemplo, Donald e Margarida atribuíram conteúdo para responsavel. Como Margarida.__init__() foi executado por último, o conteúdo de responsavel ficou como "Tia Margarida".'''



# VIDA PRÓPRIA
# Chega a hora que as crianças crescem e têm seus próprios amigos, certo? É o que vamos representar agora:

class Sobrinha(Margarida, Donald):
    def amigos(self):
        print("Huguinho, Zezinho e Luizinho")
lala = Sobrinha()
lala.amigos()
# Nesse exemplo definimos o método amigos() em Sobrinha. Portanto, ele sobrepôs o método de mesmo nome que havíamos definido em Donald.





# Mixins
''' Agora que entendemos como funciona herança múltipla, podemos falar de mixins.

Mixins são funcionalidades que você adiciona a uma classe, aproveitando o recurso de herança múltipla.

Vamos ilustrar com uma nova classe bem simples:'''
'''class Familia:
    def __init__(self, membros):
        self.membros = membros
'''
# Compondo uma família:
# ratinhos = Familia(['Mickey', 'Chiquinho', 'Francisquinho'])
# print(ratinhos.membros)

''' Não seria legal se pudéssemos usar len(ratinhos) para saber quantos membros essa família tem? Vamos tentar:'''
# Para isso usamos o 'método magico' __len__()
# Não podemos usar len(ratinhos) porque não definimos o método __len__() na classe Familia. Vamos resolver isso:

"""class Familia:
    def __init__(self, membros):
        self.membros = membros

    def __len__(self):
        return len(self.membros)

ratinhos = Familia(['Mickey', 'Chiquinho', 'Francisquinho'])
print(ratinhos.membros)
print(len(ratinhos))
"""

''' Imagine classes que tenham membros: Equipe, Dirigentes, Grupo, etc. Se quisermos essa funcionalidade em todas elas, precisaremos escrever o mesmo método __len__() em todas elas, certo? Certo, mas existe um jeito melhor, vamos usar mixins.

Se criarmos uma classe mixin, poderemos adicionar funcionalidades às classes derivadas sem esforço.

Em primeiro lugar, vamos criar uma classe para fornecer o serviço len():'''

class LenMembrosMixin:
    def __len__(self):
        return len(self.membros)

# Essa classe, por ser um mixin, não tem nada além do serviço que queremos adicionar.
# Agora a classe Familia precisa ser modificada para receber esse serviço e não mais 
# implementar __len__() nela própria. Ou seja, Familia precisa herdar de LenMembrosMixin e apagar __len__():

class Familia(LenMembrosMixin):
    def __init__(self, membros):
        print('Init de Familia')
        self.membros = membros

ratinhos = Familia(['Ratinho1', 'Ratinho2', 'Ratinho3'])
print(ratinhos.membros)
print(len(ratinhos))

''' Pronto, o mesmo efeito, com código no lugar certo.

Para esclarecer, uma classe mixin é igual a qualquer outra. A peculiaridade é que ela deve implementar apenas o serviço que irá adicionar às outras classes.'''







# EXEMPLOS DE MIXINS ÚTEIS
'''Observação: os exemplos abaixo estão simplificados para fins didáticos.

Atributos da instância em formato de dicionário:

class AsdictMixin:
    def _asdict(self):
        return self.__dict__
Nomes dos atributos existentes:

class FieldsMixin:
    def _fields(self):
        return list(self.__dict__.keys())
Representar a instância em json:

import json

class AsjsonMixin:
    def _asjson(self):
        return json.dumps(self.__dict__)
Adicionando todos esses serviços à nossa classe de exemplo:

class Familia(LenMembrosMixin, AsdictMixin, FieldsMixin, AsjsonMixin):
    def __init__(self, membros):
        self.membros = membros
Agora, podemos usá-los:

>>> ratinhos = Familia(["Mickey", "Chiquinho", "Francisquinho"])
>>> ratinhos.membros
['Mickey', 'Chiquinho', 'Francisquinho']
>>> len(ratinhos)
3
Que tal criarmos um novo atributo na família dos ratinhos e vermos como nossos mixins se comportam?

>>> ratinhos.inimigo = "Bafo de Onça"
>>> c._fields()
['membros', 'inimigo']
Certinho. Como adicionamos um inimigo, passamos a ter 2 campos.

>>> c._asdict()
{'membros': ['Mickey', 'Chiquinho', 'Francisquinho'], 'inimigo': 'Bafo de Onça'}
Perfeito. Vemos a lista de membros da família e o inimigo.

Resumindo, mixin é um conceito que permite adicionar serviços a classes através de herança múltipla, colaborando com simplificação e reaproveitamento de código em Python.

Herança múltipla em Python é muito poderosa e também muito simples.'''
