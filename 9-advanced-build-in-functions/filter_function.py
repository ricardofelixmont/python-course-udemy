# Filter function -> filter(function, iterable)  a função precisa retornar True or False dependendo do que queremos filtrar.

def starts_with_r(friend):
    return friend.startswith('R')   # Este método retorn True se frinds tiver R como primeira letra e False caso não aconteceça.

friends = ['Rolf', 'Jose', 'Randy', 'Carlos']
start_with_r = filter(starts_with_r, friends)    # só será passado para start_with_r os nomes que a função retornar True.

# a função filter retorna um iterator
# print(next(start_with_r))
# print(next(start_with_r))
# print(next(start_with_r))

# Podemos passar o valor do iterator para uma lista:
print(list(start_with_r))
# porém se tentarmos fazer novamente ele nos data uma lista vazia, pois para gerar a lista acima ele usou o for loop que roda por baixo dos panos, entao ele deixa uma lista vazia
print(list(start_with_r)) # um iterator só pode ser usado um vez




# Podemos fazer também:

friends = ['Rolf', 'Jose', 'Randy', 'Carlos']
start_with_r = filter(lambda friend: friend.startswith('R'), friends)


# podemos ainda:
another_starts_with_r = (f for f in friends if f.startswith('R'))  # Esse codigo é mais rapido pois no exemplo acima ele toma processamento criando uma lambda 
# List comprehension geralmente é mais rápido do que funções como filter() quando não é preciso criar uma função dentro dela.


def meu_filter(func, iterable):
    for f in iterable:
        if func(f):   # quer dizer que se o func(f) == True, ele vai retornar f e guardar o estado do objeto
            yield f




