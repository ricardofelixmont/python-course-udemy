#!/usr/bin/env python3.6

# Decoradores @classmethod e @classmethod

# TIPOS DE MÉTODOS EM PYTHON:
# Métodos de instância: Recebem o objeto(self) como argumento
# Métodos de classe: Recebem a classe(cls) como argumento
# Métodos estaticos: Não recebem nada como argumento.

# Digamos que temos a seguinte classe:
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

rolf = Student('Rolf', 'MIT')
rolf.marks.append(78)
rolf.marks.append(99)
print(rolf.average()) # aqui temos a sintaxe 'objeto.method()' Isto é chamado método de instância


# não precisamos de um método __init__ nas classes obrigatoriamente

# @CLASSMETHOD
# Frequentemente usamos o @classmethod quando queremos algo que quer se 
# relacionar a classe.
class Foo:
    @classmethod
    def hi(cls):  # cls guarda o valor da classe 'Foo', posso chamar de qualquer
                  # coisa porem a convensão é 'cls', pois ele se refere a clase
                  # e não ao objeto(instância da classe)
        print(cls.__name__)

my_object = Foo()
# O importante aqui é que o objeto 'my_object' não esta sendo passado como
# argumento por baixo dos panos, e sim a classe(Foo) do objeto.
my_object.hi() # aqui temos a sintaxe no background do python 'class.method()', hi() é chamado de método de classe

# @STATICMETHOD
# Utilizamos frequentemente o @staticmethod quando queremos um método que não
# usa o objeto atual ou a classe, mas algo que de alguma forma se 
# relacionada a classe.

# O metodo estatico não precisa obrigatoriamente ter parametros:
class Bar:
    @staticmethod
    def hi():
        print('Hello, I don\'t take parameters.')

another_object = Bar()
another_object.hi() # também tem a notação 'class.object' porém não recebe parametros.


# DIFERENÇAS NO USO 

class Classe:
    # funciona como um @staticmethod, porém não reconhece objetos como sendo instância da classe
    # não é recomendado usar esse tipo de método
    def printa_um(): # o certo é colocar o self como argumento
        print('1')

    # Método padrão no python, um método de instância.
    def printa_quatro(self):
        print('4')

    @classmethod
    def printa_dois(cls):
        print('2')

    @staticmethod
    def printa_tres():
        print('3')

# Parece que todos se comportam como métodos de classe 'classe.metodo()' menos o método de instacia 'printa_quatro(self)'
Classe.printa_um()
Classe.printa_dois()
Classe.printa_tres()
# Classe.printa_quatro() # Da erro pois precisa de um objeto(instância da classe) para ser usado.

print('\n')
# Testando como método de objeto
objeto = Classe()
# objeto.printa_um() # da erro, ele tenta passar o objeto como argumento e não consegue, pois o método printa_um() não recebe parametros.
objeto.printa_dois() # passa a Classe como argumento(por baixo dos panos), pois esse é um método de classe.
objeto.printa_tres() # não passa nada como parametro, porém se relaciona a classe.
objeto.printa_quatro()
# DIFERENÇA ENTRE OS MÉTODOS printa_um() e printa_tres():
# printa_um() não reconhece o objeto como sendo uma instância da classe. Já o printa_tres() reconhece o objeto como instancia da classe.



# Explicando:
class Printa:
    
    def metodo_de_instancia(self):
        print('Método de instância: objeto.metodo')
        """ este é tipo padrão de métodos em python, só é possivel utilizá-los
            quando instanciamos um objeto da classe
        """
    @classmethod
    def metodo_de_classe(cls):
        print('Método de classe: classe.metodo')
        """ este é chamado método de classe, podemos invocar o metodo como:
            classe.metodo()
            objeto.metodo()
                            As duas formas vão funcionar, porém é importante entender que por 'baixo dos panos' 
                            o python passa a 'classe' como argumento para o método e não o objeto.
        """
    @staticmethod
    def metodo_estatico():
        print('Método Estático: classe.metodo')
        """ este é o chamado método estático, podemos invocar o método como:
            classe.metodo()
            objeto.metodo()
                            As duas formas vão funcionar, porém é importante entender que por 'baixo dos panos' o python não passa
                            argumentos, porém referencia a classe de alguma maneira.
        """

    def metodo_estranho():
        print('Método que não devemos utilizar nunca =D')
        """ este método vai funcionar invocando na forma 'classe.metodo()', porém não funciona na forma 'objeto.metodo()', pois ele não reconhece 
            não recebe argumento algum. O metodo estático funciona pois mesmo escrevendo 'objeto.metodo()' o python faz 'classe.metodo()', o 
            que não acontece com esse metodo_estranho().
            *** Um especialista me respondeu que não utiliza-se isso pois o @staticmethod é uma forma de padronização essa forma de sintaxe.
        """

objeto = Printa()

objeto.metodo_de_instancia()
# Printa.metodo_de_instancia() # Não funciona pois este é um método de instância
Printa.metodo_de_classe()
Printa.metodo_estatico()

# Resumo:
# Métodos de instância são invocados apenas por um objeto.
# Métodos estáticos e de classe sempre referenciam a classe de alguma forma,
# @classmethod passa cls como argumento e esta totalmente relacionada a classe. E @staticmethod não recebe parametros e é de uso mais geral.
