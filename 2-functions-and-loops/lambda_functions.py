def add_two(x, y):
    return x + y
x = 10
y = 5
# Abaixo o exemplo de uma função anônima
lambda par1, par2: par1 + par2 # nada acontece, o python le e destroi logo em seguida para nos dar mais perfomance
# (lambda par1, par2: par1 + par2)(arg1, arg2)) -> dessa forma estamos chamando a funcao e passando argumentos
(lambda x, y: x + y)(x,y) 

# Funções simples com lambda
soma = lambda par1, par2: par1 + par2
print(soma(1,2))

# FIRST CLASS FUNCTIONS
# Uma função de primeira classe pode ser o argumento de outra função:

# Função de ordem superior
def who(data, identify):  # identify é uma função, mas nao usamos os parentesis.
    return identify(data)

# Função de primera classe
def my_identifier_function(some_data):
    return some_data['name']

print(my_identifier_function({'name':'Jose'}))

user = {'name':'Ricardo', 'surname':'Felix'}

print(who(user, my_identifier_function))#Não precisei passar o 'user' como parametro da função my_identifier_function
                                        #pois nao estamos executando a função, estamos apenas referenciando-a.
# O que o python faz:
# O segredo esta no retorno da funcao 'who()', ele aplica a função passada 'my_identifier_function' no dicionario'data'

# Podemos reescrever a função acima com uma funçao lambda:
print(who(user, lambda data: data['name']))



# EXEMPLO DE USO DE FIRS-CLASS FUNCTIONS E LAMBDA(funções anônimas)

def over_age(data, function):
    return function(data) > 18  # Deve retornar True or False

user_data = {'name':'Ricardo', 'age':'25'}

print(over_age(user_data, lambda data: int(data['age']))) # a função anônima retorna a idade como inteiro, para que
                                                         # a função over_age possa compara-la com 18 e retornar True
                                                         # ou False


