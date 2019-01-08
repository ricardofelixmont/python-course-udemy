#!/usr/bin/env python3.7

# Algumas coisas em python são mutáveis e outras imutáveis.
# Mutável: algo que pode ser alterado depois que for criado
# Imutável: Não pode ser alterado depois de criado

""" Podemos pensar: todo dado não é mutável? Quando criamos uma variável não podemos alterá-la? Podemos alterar a variavel, porém a variavel por si só não são os dados."""

friends_last_seen = {      # A variavel(espaço na memoria) 'friends_last_seen' aponta para o dicionario.
        'Ricardo':25,
        'Renata':24,
        'Rafael':23
}

# No exemplo acima o dicionario é o dado e 'friends_last_seen' é o nome dado a esse pedaço de dados.


""" Python pode nos dar o ID do objeto atraves da função id(objeto)
    o id é endereço do objeto na memoria. Sempre que rodamos o programa novamente temos um número diferente. 
    Nem sempre o id vai retornar o endereço de memoria."""

print(id(friends_last_seen))
                           

friends_last_seen = {     # Apesar de parecer ser o mesmo didicionario, o dicionario acima ainda existe quando este é criado, então precisamos de um
        'Ricardo':25,     # outro espaço na memória. Por isso os id's são diferentes.
        'Renata':24,
        'Rafael':23
}

print(id(friends_last_seen))



# Agora digamos que queremos alterar o dicionario acima: 
friends_last_seen['Ricardo'] = 0    # Aqui estamos apenas alterando o objeto e não criando outro. O que o python faz aqui é: 
                                    # friends_last_seen.__setitem__(self, 'Ricardo'). Um função altera o 'self' object.

print(id(friends_last_seen))    # O endereço de memoria continua o mesmo, a explicação para isso é que o dicionario é 
                                # uma estrutura de dados mutável no python.

# Muitas coisa em python são mutáveis, por exemplo quando criamos nossas proprias classes em python, se alterarmos um atrituto do objeto,
# ainda teremos o mesmo endereço de memoria, pois não estamos criando novos objetos, estamos apenas alterando-o.


# Entretanto existe algumas coisas imutáveis no python:
# Por exemplo um int:
my_int = 5 
# Não podemos alterar o 5, 5 é sempre 5. Lembrando que 5 é o objeto e 'my_int' é a variavel.
print(id(my_int))

my_int = my_int + 1   # my_int.__add__(self, 1): return cls(self.value += 1)
my_int += 1           # my_int.__iadd__(self, 1)
print(id(my_int))  # -> o id() do objeto int mudou pois 5 é sempre 5 e 6 é um valor totalmente diferente.




# Outro exemplo de estrutura mutável em python são as listas:
friends = ["Rofl", "Jose"]
print(id(friends))
""" Aqui teremos o mesmo id pois list é mutável, e adicionamos apenas um valor na lista e nao precisamos criar uma nova lista

    Quando usamos 'list comprehension', uma nova lista é criada."""
friends.append("Rafael")      # aqui estamos apenas mudando o objeto e não criando um novo.
print(id(friends))


# Existem poucos tipos de dados mutaveis no python, alguns exemplos abaixo:
"""
integers  -> all functions create new objects
floats
strings
tuples
"""


# Vamos ver um exemplo de tupla:
tupla = (10,20,30,40)
print(id(tupla))
tupla.pop(20)
