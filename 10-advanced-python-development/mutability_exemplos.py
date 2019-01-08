#!/usr/bin/env python3.7
friends_last_seen = {    
        'Ricardo':25,
        'Renata':24,
        'Rafael':23
}

def see_friend(friends, name):
    print(id(friends))
    friends[name] = 0

print(id(friends_last_seen))
print(id(friends_last_seen["Ricardo"]))  # Vai mostrar o id do int 25 

see_friend(friends_last_seen, "Ricardo")  
""" O que acontece aqui é o que apenas o valor de friends_last_seem é passado para a função e não
    a variável em si, então o parâmetro friends só aponta para o mesmo 
    objeto(dicionario) que friends_last_seem."""

print(id(friends_last_seen["Ricardo"]))  # Aqui o endereço mudou pois essa variavel é um inteiro.
print(id(friends_last_seen))            # O id não mudou pois o que foi alterado foi apenas um atributo do objeto dicionario e não o objeto inteiro.




# CONTINUANDO

def see_friend2(friends, name):
    print(friends == friends_last_seen)   # == compara os conteudos 
    print(friends is friends_last_seen)   # 'is' compara os id's e isto nos diz se eles sao o mesmo objeto(True) ou não(False)
    

see_friend2(friends_last_seen, 'Ricardo')


print(friends_last_seen["Ricardo"])   # Esse atributo do dicionario foi mudado.







# OUTROS EXEMPLOS

def increase_age(current_age):  # current_age aponta para 20
    current_age += 1   # criamos uma nova variavel current_age para armazenar o valor 21, porém não altera o valor da variavel age = 20


age = 20
print(id(age))
increase_age(age)
print(id(age))    # Vai retornar o mesmo valor, age é imutavel, então sempre que tentarmos alterar seu valor, na verdade estamos criando uma nova
                  # variavel.





# Agora vamos testar com uma lista:
primes = [2, 3, 5]

print(id(primes))

primes += [7, 11]   # primes = primes += [7, 11], deveria mudar, porém não é o que acontece, o id é o mesmo antes de pois da alteração.
                    # A verdade é que o que foi explicado na linha acima não acontece nesse caso. O que acontece na verdade no background o python é
                    # primes = primes.__iadd__([7, 11])

print(id(primes))
